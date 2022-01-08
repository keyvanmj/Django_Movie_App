from django.urls import path
from .views import (
    home_view,header,footer,sidebar
)


app_name = 'Main'
urlpatterns = [
    path('',home_view,name='home'),
    path('header',header,name='header_partial'),
    path('footer',footer,name='footer_partial'),
    path('sidebar',sidebar,name='sidebar_partial'),
]