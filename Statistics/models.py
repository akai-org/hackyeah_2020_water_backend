from django.db import models

from Profiles.models import Profile


class Question(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image1_url = models.URLField()
    image2_url = models.URLField()
