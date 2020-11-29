from django.db import models

from Profiles.models import Profile


class StatisticAnswer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField()


class StatisticType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField()
    exp_value = models.FloatField()
    water_saving_per_unit = models.FloatField()
    answers = models.ManyToManyField(StatisticAnswer)


class Question(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image1_url = models.URLField()
    image2_url = models.URLField()
    statistics = models.ManyToManyField(StatisticType)


class ProfileStatistic(models.Model):
    created_at = models.DateTimeField()
    water_saved = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    statistic_type = models.ForeignKey(StatisticType, on_delete=models.CASCADE)
