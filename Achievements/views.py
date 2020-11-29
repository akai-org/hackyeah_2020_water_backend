from rest_framework.decorators import api_view
from rest_framework.response import Response

from Achievements.models import *


@api_view(http_method_names=['POST'])
def get_achievements(request):
    user_id = request.data['id']
    profile_id = Profile.objects.filter(user_id=user_id).values()[0]['id']
    users_collected_achievements_id = [a['achievement_id'] for a in
                                       CollectedAchievement.objects.filter(profile=profile_id).values()]
    achievement_list = [
        {'id': a['id'],
         'name': a['name'],
         'description': a['description'],
         'image_url': a['image_url'],
         'level': a['level'],
         'exp_value': a['exp_value'],
         'collected_at': None} for a in
        Achievement.objects.all().values()]

    for ach in achievement_list:
        ach_id = ach['id']
        if ach_id in users_collected_achievements_id:
            ach['collected_at'] = \
                CollectedAchievement.objects.filter(profile=profile_id, achievement=ach_id).values()[0][
                    'collected_at']
    return Response(achievement_list)
