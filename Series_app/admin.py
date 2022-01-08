from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import Series


class SeriesAdmin(AdminVideoMixin,admin.ModelAdmin):
    list_of_display = ['title', 'release_date']
    list_display = ['title', 'release_date', 'thumbnail_tag']

admin.site.register(Series,SeriesAdmin)
