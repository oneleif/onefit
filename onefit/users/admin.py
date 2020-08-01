from django.contrib import admin
from .models import Profile
from django.apps import apps

admin.site.register(Profile)
admin.site.register(apps.get_model('workouts','Workout'))
