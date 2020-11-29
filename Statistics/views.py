from rest_framework.decorators import api_view
from rest_framework.response import Response

from Statistics.models import *


@api_view(http_method_names=['GET'])
def get_questions(request):
    return Response(Question.objects.all().values())


@api_view(http_method_names=['POST'])
def send_answers_response(request):
    user_id = request.data['id']
    profile = Profile.objects.filter(user_id=user_id).values()[0]
    saved_water = 0
    gained_xp = 0
    bath_choice = request.data['answers'][0]['answer']
    if bath_choice == 1:
        saved_water += 150
        gained_xp += 300
    washing_up_choice = request.data['answers'][1]['answer']
    if washing_up_choice == 1:
        saved_water += 85
        gained_xp += 170
    teethbrushing_choice = request.data['answers'][2]['answer']
    if teethbrushing_choice == 1:
        saved_water += 15
        gained_xp += 30
    profile['gained_xp'] += gained_xp
    profile['saved_water'] += saved_water
    profile.save()
    return Response({'saved_water': saved_water, 'gained_xp': gained_xp})
