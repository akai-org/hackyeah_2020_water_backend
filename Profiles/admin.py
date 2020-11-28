from django.contrib import admin

# Register your models here.
from Profiles.models import Profile

admin.site.register([Profile])
