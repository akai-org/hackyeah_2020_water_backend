from django.contrib import admin

# Register your models here.
from Statistics.models import StatisticAnswer, StatisticType, Question, ProfileStatistic

admin.site.register([StatisticAnswer, StatisticType, Question, ProfileStatistic])