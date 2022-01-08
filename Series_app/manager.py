from django.contrib.postgres.search import SearchQuery, SearchVector, SearchHeadline
from django.db import models
from django.db.models import Sum, Q, Count
from django.http import Http404


class SeriesManager(models.Manager):
    def all_with_related_person(self):
        qs = self.get_queryset()
        qs = qs.select_related('director')
        qs = qs.prefetch_related('writers', 'actors')
        return qs

    def all_with_related_persons_and_score(self):
        qs = self.all_with_related_person()
        qs = qs.annotate(score=Sum('vote__value'))
        return qs


    def top_movies(self, limit=10):
        qs = self.get_queryset()
        qs = qs.annotate(vote_sum=Sum('vote__value'))
        qs = qs.exclude(vote_sum=None)
        qs = qs.order_by('-vote_sum')
        qs = qs[:limit]
        return qs

    def search_series(self, q):
        if q != '':
            query = SearchQuery(q)
            vector = SearchVector('title')
            qs = self.get_queryset().annotate(
                headline=SearchHeadline('description', query, start_sel='<span class="text_search">', stop_sel='</span>'),
                search=vector).filter(
                Q(title__icontains=q) | Q(genre__title__icontains=q)).distinct().order_by(
                'search','-headline')
            return qs
        else:
            return self.get_queryset().all()

    def get_by_category(self, slug):
        series_genre = (
                Q(genre__title__icontains=slug)|
                Q(genre__series__series_slug__iexact=slug) |
                Q(genre__parent__slug__iexact=slug) |
                Q(genre__parent__parent__slug__iexact=slug)
        )
        return self.get_queryset().filter(series_genre).distinct().order_by('-date')

    def popular_series(self):
        return self.get_queryset().annotate(count=Count('series_hits')).order_by('-count', '-date')

    def top_rated_series(self):
        qs = self.get_queryset()
        qs = qs.order_by('-imdb_rate')
        return qs

    def release_date(self):
        qs = self.get_queryset()
        qs = qs.order_by('-release_date')
        return qs

    def filter_series(self, filter_series):
        if 'popular' == filter_series:
            return self.popular_series()
        if 'top_rated' == filter_series:
            return self.top_rated_series()
        if 'release_date' == filter_series:
            return self.release_date()
        else:
            raise Http404('not found')

    def sidebar_filter_series(self,data):
        if data('type_select') == 'All':
            queryset = self.get_queryset().filter(
                genre__title=data('genre_select'),
                release_date__icontains=data('release_date')
            )
        else:
            queryset = self.get_queryset().filter(
                genre__title=data('genre_select'),
                types__iexact=data('type_select'),
                release_date__icontains=data('release_date')
            )
        return queryset

    def person_series(self,slug):
        person = (
            Q(cast__slug=slug) |
            Q(creator__slug=slug)
        )
        return self.get_queryset().filter(person).distinct().order_by('-release_date')