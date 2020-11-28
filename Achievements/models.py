from django.db import models

from Profiles.models import Profile
from Statistics.models import StatisticType


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Achievement(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField()
    exp_value = models.FloatField()
    tags = models.ManyToManyField(Tag)
    statistic = models.ForeignKey(StatisticType, on_delete=models.CASCADE, null=True)


class CollectedAchievement(models.Model):
    collected_at = models.DateTimeField()
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
