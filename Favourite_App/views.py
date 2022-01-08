from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from accounts.decorators import ajax_login_required
from .models import Favourite
from Movie_app.models import Movie
from Series_app.models import Series

@ajax_login_required
def add_to_favourite(request,slug,pk):
    favourite_queryset = None
    obj_url = None
    movie = None
    series = None
    try:
        movie = get_object_or_404(Movie, slug=slug, pk=pk)
        favourite_queryset = Favourite.objects.filter(
            movies_id=pk, movies__slug=slug, user=request.user)
        obj_url = reverse('Movies:movie_detail', kwargs={'slug': slug, 'pk': pk})
    except:
        series = get_object_or_404(Series, series_slug=slug, pk=pk)
        favourite_queryset = Favourite.objects.filter(
            series_id=pk, series__series_slug=slug, user=request.user)
        obj_url = reverse('Series:series_detail_view', kwargs={'slug': slug, 'pk': pk})
    if request.is_ajax():
        if movie:
            # obj_url = movie.get_absolute_url()
            if favourite_queryset.exists():
                favourite_queryset.delete()
                status = 'Deleted'
                msg = f'{movie.title} ({movie.release_date}) Removed From Favourites'
            else:
                Favourite.objects.get_or_create(
                    movies_id=movie.pk,
                    movies=movie, user=request.user,
                )
                status = 'Created'
                msg = f'{movie.title} ({movie.release_date}) Added To Favourites'
        elif series:
            # obj_url = series.get_absolute_url()
            if favourite_queryset.exists():
                favourite_queryset.delete()
                status = 'Deleted'
                msg = f'{series.title} ({series.release_date}) Removed From Favourites'


            else:
                Favourite.objects.get_or_create(
                    series_id=series.pk,
                    series=series, user=request.user,
                )
                status = 'Created'
                msg = f'{series.title} ({series.release_date}) Added To Favourites'
        else:
            return None

        context = {
            'slug':slug,
            'pk':pk,
            'status':status,
            'msg':msg,
        }
        return JsonResponse({'data':context})
    return redirect(obj_url)


class FavouriteList(ListView,LoginRequiredMixin):
    template_name = 'favourite/favourite_list.html'
    paginate_by = 5
    model = Favourite

    @method_decorator(ajax_login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super(FavouriteList, self).dispatch(request,*args,**kwargs)

    def get_queryset(self):
        favourite = Favourite.objects.filter(
            user=self.request.user).order_by(
            '-time_stamp'
        )
        chained_fav_obj = list((x.movies, x.series) for x in favourite)
        chained_items = [x for x in chained_fav_obj for x in x]
        object_list = list(filter(None, chained_items))
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(FavouriteList, self).get_context_data(*args, **kwargs)
        context['objects_count'] = self.object_list.__len__()
        context['queryset_objects'] = [s.get_obj_model_name for s in self.object_list]
        return context
