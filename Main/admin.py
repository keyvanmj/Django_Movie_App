from django.contrib import admin
from accounts.models import Profile
from .models import ScreenShot

class ScreenShotInline(admin.TabularInline):
    model = ScreenShot


admin.site.register(ScreenShot)
admin.site.register(Profile)