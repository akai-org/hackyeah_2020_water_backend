from rest_framework import viewsets

from Achievements.models import Achievement, CollectedAchievement
from Achievements.serializers import AchievementSerializer, CollectedAchievementSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class CollectedAchievementViewSet(viewsets.ModelViewSet):
    queryset = CollectedAchievement.objects.all()
    serializer_class = CollectedAchievementSerializer
