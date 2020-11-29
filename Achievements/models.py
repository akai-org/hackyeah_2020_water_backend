from django.db import models

from Profiles.models import Profile


class Achievement(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField()
    exp_value = models.FloatField()


class CollectedAchievement(models.Model):
    collected_at = models.DateTimeField()
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
