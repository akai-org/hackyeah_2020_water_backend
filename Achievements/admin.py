from django.contrib import admin

# Register your models here.
from Achievements.models import CollectedAchievement, Achievement
from Profiles.models import Profile

admin.site.register([Achievement, CollectedAchievement])