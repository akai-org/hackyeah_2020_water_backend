from django.contrib import admin

# Register your models here.
from Habits.models import HabitsEntry, SelectedHabits, HabitType

admin.site.register([HabitType, SelectedHabits, HabitsEntry])