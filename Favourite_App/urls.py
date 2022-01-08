from django.urls import path

from .views import add_to_favourite,FavouriteList


app_name = 'Favourite'
urlpatterns = [
    path('<str:slug>/<int:pk>/',add_to_favourite,name='add_favourite'),
    path('favourite_list/',FavouriteList.as_view(),name='favourite_list'),
]