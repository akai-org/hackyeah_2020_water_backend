from rest_framework import serializers
from Achievements import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = [
            'name'
        ]


class AchievementSerializer(serializers.ModelSerializer):
    tags = serializers.ListField()

    class Meta:
        model = models.Achievement
        fields = [
            'name',
            'description',
            'image_url',
            'exp_value',
            'tags',
            'statistic',
        ]


class CollectedAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CollectedAchievement
        fields = [
            'collected_at',
            'achievement',
            'profile',
        ]
