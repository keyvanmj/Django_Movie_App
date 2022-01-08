from itertools import chain

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse

from Movie_app.models import Movie
from Series_app.models import Series
from Vote_app.models import Vote


class VoteMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def combine_movie_series_qs(self):
        movie_qs = Movie.objects.all().filter(slug=self.kwargs['obj_slug'])
        series_qs = Series.objects.all().filter(series_slug=self.kwargs['obj_slug'])
        multi_qs = list(chain(movie_qs, series_qs))
        return multi_qs

    def combine_vote_obj(self):
        try:
            vote_obj = Vote.objects.filter(
                movie_id=self.get_object().pk,movie__slug=self.get_object().slug,
                user=self.request.user
            )
        except:
            vote_obj = Vote.objects.filter(
                series_id=self.get_object().pk, series__series_slug=self.get_object().series_slug,
                user=self.request.user
            )
        return vote_obj

    def get_object(self, queryset=None):
        try:
            qs = get_object_or_404(Series, series_slug=self.kwargs['obj_slug'], pk=self.kwargs['obj_id'])
        except:
            qs = get_object_or_404(Movie, slug=self.kwargs['obj_slug'], pk=self.kwargs['obj_id'])
        return qs

    def get_success_url(self):
        try:
            movie_id = self.get_object().pk
            movie_slug = self.get_object().slug
            return reverse('Movies:movie_detail', kwargs={'slug': movie_slug, 'pk': movie_id})
        except:
            series_id = self.get_object().pk
            series_slug = self.get_object().series_slug
            return reverse('Series:series_detail_view', kwargs={'slug': series_slug, 'pk': series_id})