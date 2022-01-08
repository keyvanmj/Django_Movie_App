import json
from itertools import chain
from django.core import serializers
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView
from Movie_Category.forms import SelectGenreFilterForm
from Movie_Category.models import Genre
from Movie_app.models import Movie
from Movies_WebApp import settings
from Series_app.models import Series
from Main.utils import merging_model


class JsonResponseMixin:
    def render_to_json_response(self,context,**response_kwargs):
        return JsonResponse(self.get_data(context),**response_kwargs)

    def get_data(self,context):
        return context


class GenreView(ListView):
    template_name = 'movie/top_movies_list.html'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self):
        slug = self.kwargs['hierarchy']
        types = self.kwargs['type']
        movies_query = Movie.objects.get_by_category(slug)
        series_query = Series.objects.get_by_category(slug)

        # insert Movies first
        if 'Movie' == types:
            merge_models = merging_model(movies_query,series_query)

        # insert Series first
        elif 'Series' == types:
            merge_models = merging_model(series_query,movies_query)

        elif 'type=Movie' == types:
            merge_models = movies_query

        elif 'type=Series' == types:
            merge_models = series_query

        else:
            raise Http404()

        return merge_models

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(GenreView, self).get_context_data(*args, **kwargs)
        context['category_slug'] = self.kwargs['hierarchy']
        return context

class SelectFilterView(ListView,JsonResponseMixin):
    template_name = 'movie/movie_list.html'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self):
        form = SelectGenreFilterForm(data=self.request.GET or None)
        merge_models = None
        if form.is_valid():
            g_data = form.cleaned_data.get

            movies_query = Movie.objects.sidebar_filter_movies(data=g_data)

            series_query = Series.objects.sidebar_filter_series(data=g_data)

            merge_models = merging_model(movies_query,series_query)

        return merge_models

    def get(self,request,*args,**kwargs):
        self.object_list = self.get_queryset()
        try:
            list_query_set = [x.types for x in self.object_list]

            str_qs = ' , '.join(list_query_set)
            if 'Series' == str_qs:
                queryset_length = f'Found <span>{len(list_query_set)}</span> Series'

            elif 'Movie' == str_qs:
                queryset_length = f'Found <span>{len(list_query_set)}</span> Movies'

            elif 'Movie' and 'Series' in str_qs:
                queryset_length = f'Found <span>{len(list_query_set)}</span> Movies & Series'

            elif str_qs == None or str_qs == [] or str_qs == '':
                queryset_length = f'Nothing Found'

            else:
                queryset_length = f'Found <span>{len(list_query_set)}</span> Movies'

            path = self.request.get_full_path()
            form = SelectGenreFilterForm(data=self.request.GET or None)
            queryset = self.object_list
            page_size = self.get_paginate_by(queryset)
            page = None
            current_page = None
            is_paginated = None
            if page_size:
                paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)

            data = {
                'obj_count': queryset_length,
                'view_path': path,
                'template': render_to_string('list_templates/object_list_template.html', context={'object_list': queryset}),
                'type_select': self.request.GET.get('type_select'),
                'form':f'{form}',
                'object_list':serializers.serialize('json',self.object_list),
                'paginate_template':render_to_string('shared/paginate/paginate.html',context={'page_obj':page}),
                'current_page':page.number,
                'is_paginated':is_paginated
            }
            return JsonResponse(data)
        except:
            return JsonResponse({'msg':'not found'})



