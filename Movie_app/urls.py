from django.urls import path
from .views import (
    MovieList, MovieDetail, MovieImageUpload, TopMovies, MovieFilterListView
)
app_name = 'Movies'
urlpatterns = [
    path('movie_list/',MovieList.as_view(),name='movie_list'),
    path('movie_list/<str:filter>', MovieFilterListView.as_view(), name='filter_movie_list'),
    path('top_movies/',TopMovies.as_view(),name='top_movies_list'),
    path('movie_detail/<slug:slug>/<int:pk>/',MovieDetail.as_view(),name='movie_detail'),
    path('movie/<slug:movie_slug>/<int:movie_id>',MovieImageUpload.as_view(),name='movie_image_upload'),
]
