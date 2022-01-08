from django.db import models
from django.db.models import Sum, Q, Count, Aggregate, Max
from django.contrib.postgres.search import SearchHeadline, TrigramSimilarity, SearchQuery, SearchVector, SearchRank
from django.http import Http404


class MovieManager(models.Manager):
    def all_with_related_person(self):
        qs = self.get_queryset()
        qs = qs.select_related()
        qs = qs.prefetch_related('director','cast')
        return qs

    def all_with_related_persons_and_score(self):
        qs = self.all_with_related_person()
        qs = qs.annotate(score=Sum('vote__value'))
        return qs

    def top_movies(self,limit=10):
        qs = self.get_queryset()
        qs = qs.annotate(vote_sum=Max('vote__value'),rate_sum=Sum('rate__rate'))
        qs = qs.exclude(vote_sum=None,rate_sum=None)
        qs = qs.order_by('rate_sum','-vote_sum')
        qs = qs[:limit]
        return qs

    def search_movies(self,q):
        if q != '':
            query = SearchQuery(q)
            vector = SearchVector('title')
            qs = self.get_queryset().annotate(headline=SearchHeadline('plot',query,start_sel='<span class="text_search">',stop_sel='</span>'),
                search=vector).filter(Q(title__icontains=q) | Q(genre__title__icontains=q)).distinct().order_by('search','-headline')
            return qs
        else:
            return self.get_queryset().all()

    def get_by_category(self,slug):
        movie_genre = (
            Q(genre__slug__iexact=slug) |
            Q(genre__parent__slug__iexact=slug) |
            Q(genre__parent__parent__slug__iexact=slug)
        )
        return self.get_queryset().filter(movie_genre).distinct().order_by('-created')

    def popular_movies(self):
        return self.get_queryset().annotate(count=Count('movie_hits')).order_by('-count','-date')

    def top_rated_movies(self):
        qs = self.get_queryset()
        qs = qs.order_by('-imdb_rating')
        return qs

    def release_date(self):
        qs = self.get_queryset()
        qs = qs.order_by('-release_date','-created')
        return qs

    def filter_movies(self,filter_movie):
        if 'popular' == filter_movie:
            return self.popular_movies()
        if 'top_rated' == filter_movie:
            return self.top_rated_movies()
        if 'release_date' == filter_movie:
            return self.release_date()
        else:
            raise Http404('not found')


    def sidebar_filter_movies(self,data):

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

    def person_movies(self,slug):
        person = (
            Q(cast__slug=slug) |
            Q(director__slug=slug)
        )
        return self.get_queryset().filter(person).distinct().order_by('-release_date')