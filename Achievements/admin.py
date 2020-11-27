from django.contrib import admin

# Register your models here.
from Achievements.models import CollectedAchievement, Achievement, Tag
from Profiles.models import Profile

admin.site.register([Tag, Achievement, CollectedAchievement])