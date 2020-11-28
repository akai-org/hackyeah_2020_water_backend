from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from Achievements.models import *


@api_view(http_method_names=['POST'])
def achievement_list(request):
    user_id = request.data['id']
    profile_id = Profile.objects.filter(user_id=user_id).values()[0]
    all_achievements = Achievement.objects.all().values()

    return Response()
