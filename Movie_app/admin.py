from django.contrib import admin
from .models import Movie,MovieImage
from embed_video.admin import AdminVideoMixin



class MovieAdmin(AdminVideoMixin,admin.ModelAdmin):
    list_of_display = ['title','release_date']
    list_display = ['title', 'release_date', 'thumbnail_tag']


admin.site.register(Movie,MovieAdmin)
admin.site.register(MovieImage)