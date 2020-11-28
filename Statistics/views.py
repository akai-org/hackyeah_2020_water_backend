from rest_framework.decorators import api_view
from rest_framework.response import Response

from Statistics.models import *


@api_view(http_method_names=['POST'])
def get_stats(request):
    user_id = request.data['id']
    response_body = {}
    profile_id = Profile.objects.filter(user_id=user_id).values()[0]['id']
    user_stats_ids = ProfileStatistic.objects.filter(profile=profile_id).values()
    user_stats = []

    return Response()
