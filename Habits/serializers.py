from rest_framework import serializers
from Habits import models


class HabitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HabitType
        fields = []


class SelectedHabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SelectedHabits
        fields = []


class HabitsEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HabitsEntry
        fields = []
