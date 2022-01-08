from django.contrib import admin
from .models import Vote
from .models import Rate


admin.site.register(Vote)
admin.site.register(Rate)