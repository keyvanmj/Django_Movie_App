from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from Movie_app.models import Movie
from Movies_WebApp import settings
from Series_app.models import Series
from Main.utils import merging_model



class PersonMovieOrSeriesList(ListView):
    template_name = 'movie/top_movies_list.html'
    paginate_by = settings.PAGINATE_BY

    def render_to_response(self, context, **response_kwargs):
        print(self.object_list)
        if self.object_list == None or self.object_list == []:
            return redirect(reverse('Main:home'))
        return super(PersonMovieOrSeriesList, self).render_to_response(context,**response_kwargs)

    def get_queryset(self):
        role = self.kwargs['role']
        slug = self.kwargs['slug']
        movie_qs = Movie.objects.person_movies(slug)
        series_qs = Series.objects.person_series(slug)
        not_role = role != 'director' and role != 'creator' and role != 'actor'
        if not_role:
            merge_qs = []
        merge_qs = merging_model(movie_qs,series_qs)
        cast = None
        if role == 'actor':
            cast = [x.cast.filter(slug=slug) for x in merge_qs]
        elif role == 'creator':
            cast = [x.creator.filter(slug=slug) for x in series_qs]
        elif role == 'director':
            cast = [x.director.filter(slug=slug) for x in movie_qs]
        try:
            cast = list(filter(None,cast))
        except:
            pass
        if cast == [] or cast is None:
            merge_qs = []
        return merge_qs

    def get_context_data(self, *args, **kwargs):
        context = super(PersonMovieOrSeriesList, self).get_context_data(*args,**kwargs)
        context['person_slug'] = self.kwargs['slug']
        context['person_role'] = self.kwargs['role']
        return context