from itertools import chain
from django.shortcuts import render

from Movie_Category.models import Genre
from Movie_app.models import Movie
from Movie_app.utils import my_grouper
from Series_app.models import Series



def home_view(request):
    movie = Movie.objects.all().order_by('-created')
    grouped_movies = my_grouper(4,movie)
    series = Series.objects.all().order_by('-date')
    merged_models = list(chain(movie[:4],series[:4]))
    # filter for movies
    popular_movies = Movie.objects.popular_movies()
    top_rated_movies = Movie.objects.top_rated_movies()
    release_date_movies = Movie.objects.release_date()
    filter_movie = Movie.objects.filter_movies('popular')
    # filter for series
    popular_series = Series.objects.popular_series()
    filter_series = Series.objects.filter_series('popular')
    top_rated_series = Series.objects.top_rated_series()
    release_date_series = Series.objects.release_date()
    context = {
        'movies':movie[:6],
        'grouped_movies':grouped_movies,
        'series':series,
        # filter for movies
        'popular_movies':popular_movies,
        'filter_movie':filter_movie,
        'top_rated_movie':top_rated_movies,
        'release_date_movies':release_date_movies,
        # filter for series
        'popular_series':popular_series,
        'filter_series':filter_series,
        'top_rated_series':top_rated_series,
        'release_date_series':release_date_series,
        'merged_models':[x for x in merged_models],
        'category':Genre.objects.all()
    }

    return render(request,'home/home.html',context)

def header(request,*args,**kwargs):
    context = {}
    return render(request,'header/header.html',context)

def footer(request,*args,**kwargs):
    context = {}
    return render(request,'footer/footer.html',context)

def sidebar(request):
    context = {}
    return render(request,'shared/sidebar.html',context)