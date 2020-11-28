from rest_framework.decorators import api_view
from rest_framework.response import Response

from Profiles.models import *


@api_view(http_method_names=['POST'])
def get_profile(request):
    user_id = request.data['id']
    user_profile = Profile.objects.filter(user_id=user_id).values()[0]
    return Response(user_profile)
