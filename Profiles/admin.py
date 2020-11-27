from django.contrib import admin

# Register your models here.
from Profiles.models import Profile, Voivodeship

admin.site.register([Profile, Voivodeship])