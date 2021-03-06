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
    gained_exp = 0
    bath_choice = request.data['answer_1']
    if bath_choice == 1:
        saved_water += 150
        gained_exp += 300
    washing_up_choice = request.data['answer_2']
    if washing_up_choice == 1:
        saved_water += 85
        gained_exp += 170
    teethbrushing_choice = request.data['answer_3']
    if teethbrushing_choice == 1:
        saved_water += 30
        gained_exp += 60
    profile['gained_exp'] += gained_exp
    profile['saved_water'] += saved_water
    Profile(**profile).save()
    return Response({'saved_water': saved_water, 'gained_exp': gained_exp})
