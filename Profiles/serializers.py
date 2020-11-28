from django.contrib.auth.models import User
from rest_framework import serializers

from Profiles import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Profile
        fields = [
            'user',
            'avatar_url',
            'age',
        ]
