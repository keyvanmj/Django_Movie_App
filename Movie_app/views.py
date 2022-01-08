import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from Comment_app.forms import CommentForm
from Comment_app.models import CommentModel
from Comment_app.views import PostComment
from Favourite_App.models import Favourite
from Movie_Category.forms import SelectGenreFilterForm
from Movies_WebApp import settings
from Vote_app.forms import VoteForm
from Vote_app.models import Vote, Rate
from accounts.decorators import ajax_login_required
from .forms import MovieImageForm
from .models import Movie

class LoginOnly(View):

    @method_decorator(ajax_login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MovieList(ListView,LoginRequiredMixin):
    template_name = 'movie/movie_list.html'
    model = Movie
    paginate_by = settings.PAGINATE_BY


    def get_queryset(self):
        return Movie.objects.all().order_by('-created')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(MovieList, self).get_context_data(*args,**kwargs)
        side_filter_form = SelectGenreFilterForm(data=self.request.GET or None)
        context['side_filter_form'] = side_filter_form
        context['object_length'] = self.get_queryset().count()

        return context

class MovieDetail(DetailView):
    template_name = 'movie/movie_detail.html'
    model = Movie
    form_class = CommentForm

    def get_queryset(self):
        return Movie.objects.all_with_related_persons_and_score()

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        pk = self.kwargs['pk']
        movie_obj = get_object_or_404(Movie,slug=slug,pk=pk)

        ip_address = self.request.ip_address
        if ip_address not in movie_obj.movie_hits.all():
            movie_obj.movie_hits.add(ip_address)
        return movie_obj


    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super(MovieDetail, self).get_context_data(**kwargs)

        """like and dislike"""
        vote = None
        vote_form_url = None
        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                movie=self.object, user=self.request.user
            )
            if vote.id:
                vote_form_url = reverse(
                    'Vote:update_vote',
                    kwargs={'obj_slug': vote.movie.slug,
                    'obj_id': vote.movie.id, 'pk': vote.id}
                )
            else:
                vote_form_url = reverse(
                    'Vote:create_vote',
                    kwargs={'obj_slug': vote.movie.slug,
                    'obj_id': self.object.id}
                )

        vote_form = VoteForm(value=self.object.get_vote_value(request=self.request))
        context['vote_form'] = vote_form
        context['vote_form_url'] = vote_form_url
        context['vote_value'] = self.object.get_vote_value(request=self.request)

        related_movie = related_movies(self.get_object(),self.kwargs['pk'])
        context['related_movies'] = random.sample(list(related_movie),len(related_movie))


        """star rating for Movies"""

        if self.request.user.is_authenticated:
            rate_object = Rate.objects.get_rate_or_unsaved_blank_rate(
                movie=self.object, user=self.request.user
            )

            rate_form_url = reverse(
                'Vote:star_rate',kwargs={'obj_slug': self.object.slug, 'obj_id': self.object.id}
            )
            rate = 0
            if rate_object:
                rate = rate_object[0].rate
            context['review_rate'] = rate
            context['star_rate_form'] = rate_form_url

        context['rate_avg'] = Rate.objects.get_rate_avg(obj_id=self.kwargs['pk'],obj_slug=self.kwargs['slug'])

        context['image_form'] = self.movie_image_form()

        context['comment_form'] = CommentForm()
        context['all_comments'] = CommentModel.objects.filter(movie=self.get_object()).order_by('-created_on')

        if self.request.user.is_authenticated:
            favourite_queryset = Favourite.objects.filter(user=self.request.user,movies_id=self.object.pk,movies__slug=self.object.slug)
            context['favourite'] = favourite_queryset

        return context

    def movie_image_form(self):
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            return MovieImageForm(auto_id='id_upload_%s_movies')
        return None

    def post(self, request, *args, **kwargs):
        comment = PostComment.as_view(template_name=self.template_name)
        return comment(request,*args,**kwargs)


class MovieImageUpload(LoginRequiredMixin, CreateView):
    form_class = MovieImageForm

    def get_initial(self):
        initial = super(MovieImageUpload, self).get_initial()
        initial['user'] = self.request.user.id
        initial['movie'] = self.kwargs['movie_id']
        return initial

    def render_to_response(self, context, **response_kwargs):
        movie_slug = self.kwargs['movie_slug']
        movie_id = self.kwargs['movie_id']
        movie_detail_url = reverse('Movies:movie_detail', kwargs={'slug': movie_slug, 'pk': movie_id})
        return redirect(to=movie_detail_url)

    def get_success_url(self):
        movie_slug = self.kwargs['movie_slug']
        movie_id = self.kwargs['movie_id']
        movie_detail_url = reverse('Movies:movie_detail', kwargs={'slug': movie_slug, 'pk': movie_id})
        return movie_detail_url


class TopMovies(ListView):
    template_name = 'movie/top_movies_list.html'
    paginate_by = 20

    def get_queryset(self):
        limit = 250
        query_set = Movie.objects.top_movies(limit=limit)
        return query_set

    def get_context_data(self, *args, **kwargs):
        context = super(TopMovies, self).get_context_data(*args,**kwargs)
        side_filter_form = SelectGenreFilterForm(data=self.request.GET or None)
        context['side_filter_form'] = side_filter_form
        context['object_length'] = self.get_queryset().count()

        return context

class MovieFilterListView(ListView):
    template_name = 'movie/movie_list.html'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self):
        return Movie.objects.filter_movies(filter_movie=self.kwargs['filter'])

    def get_paginate_by(self, queryset):
        return self.paginate_by

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(MovieFilterListView, self).get_context_data(*args, **kwargs)
        context['filter_url'] = self.kwargs['filter']
        return context



def related_movies(movie,pk):
    movies = Movie.objects.filter(
        Q(director__in=movie.director.all())|
        Q(genre__in=movie.genre.all()) |
        Q(cast__in=movie.cast.all())
    ).distinct().exclude(pk=pk).order_by('-director')
    return movies[:8]