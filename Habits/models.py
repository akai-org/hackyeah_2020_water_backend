from django.db import models

from Profiles.models import Profile
from Statistics.models import StatisticType


class HabitType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField()
    exp_value = models.FloatField()
    statistic = models.ForeignKey(StatisticType, on_delete=models.CASCADE, null=True)


class SelectedHabits(models.Model):
    is_active = models.BooleanField()
    statistic = models.ForeignKey(StatisticType, on_delete=models.CASCADE, null=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class HabitsEntry(models.Model):
    created_at = models.DateField()
    selected_habits = models.ForeignKey(SelectedHabits, on_delete=models.CASCADE)
