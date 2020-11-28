from rest_framework import serializers
from Statistics import models


class StatisticAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StatisticAnswer
        fields = [
            'name',
            'description',
            'image_url'
        ]


class StatisticTypeSerializer(serializers.ModelSerializer):
    class Meta:
        pass


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = [
            'name',
            'content'
        ]


class ProfileStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        pass
