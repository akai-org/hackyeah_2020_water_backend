import datetime

from django.conf import settings
from requests.exceptions import HTTPError
from rest_framework import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from social_django.utils import psa


class SocialSerializer(serializers.Serializer):
    accessToken = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )


@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
@psa()
def exchange_token(request, backend):
    serializer = SocialSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            nfe = settings.NON_FIELD_ERRORS_KEY
        except AttributeError:
            nfe = 'non_field_errors'
        try:
            user = request.backend.do_auth(serializer.validated_data['accessToken'])
        except HTTPError as e:
            return Response(
                {'errors': {
                    'token': 'Invalid token',
                    'detail': str(e),
                }},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                last_login = user.last_login
                user.last_login = datetime.datetime.now()
                user.save()
                return Response({'token': token.key,
                                 'user': {
                                     'id': user.id,
                                     'first_name': user.first_name,
                                     'last_name': user.last_name,
                                     'avatar_url': user.profile.avatar_url,
                                     'email': user.username,
                                     'created': created,
                                     'last_login': last_login
                                 }})
            else:
                return Response(
                    {'errors': {nfe: 'This user account is inactive'}},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {'errors': {nfe: "Authentication Failed"}},
                status=status.HTTP_400_BAD_REQUEST,
            )

