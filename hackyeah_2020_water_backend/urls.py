from django.contrib import admin
from django.urls import path, include
from Profiles.views import *
from Achievements.views import *
from Statistics.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('profile/', get_profile),
    path('achievements/', get_achievements),
    path('questions/', get_questions),
    path('answers/', send_answers_response)
]
