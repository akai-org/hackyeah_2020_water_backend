from django.contrib import admin


from Achievements.models import CollectedAchievement, Achievement

admin.site.register([Achievement, CollectedAchievement])