from django.urls import path
from .views import PersonMovieOrSeriesList


app_name = 'Person'
urlpatterns = [
    path('<str:role>/<slug:slug>',PersonMovieOrSeriesList.as_view(),name='person_movies_or_series_list'),
]
