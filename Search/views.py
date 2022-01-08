from collections import defaultdict
from itertools import chain
from Main.utils import merging_model
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, TemplateView
from Movie_app.models import Movie, MovieImage
from Movies_WebApp import settings
from Series_app.models import Series


class AjaxSearch(TemplateView):
    template_name = 'search/search_tag.html'
    def get(self, request, *args, **kwargs):
        res = None
        if self.request.is_ajax and self.request.GET:
            q = self.request.GET.get('q')
            movie_obj = Movie.objects.search_movies(q)[:10]
            series_obj = Series.objects.search_series(q)[:10]
            merge_query = merging_model(movie_obj, series_obj)[:5]
            serialize_model_object = serializers.serialize('json', merge_query)
            result_search_template = render_to_string(template_name='search/result_search.html',context={'result':merge_query})
            return JsonResponse({'obj':serialize_model_object,'result_search':result_search_template})

        return super(AjaxSearch, self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(AjaxSearch, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class SearchView(ListView):
    template_name = 'list_templates/search_list.html'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self):
        q = self.request.GET.get('q')
        movies_queryset = Movie.objects.search_movies(q)
        series_queryset = Series.objects.search_series(q)
        merge_queries = merging_model(movies_queryset,series_queryset)
        return merge_queries

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(*args,**kwargs)
        q = self.request.GET.get('q')
        context['object_list_count'] = self.get_queryset().__len__()
        context['q'] = q
        return context