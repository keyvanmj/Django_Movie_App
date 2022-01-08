import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from Comment_app.forms import CommentForm
from Comment_app.models import CommentModel
from Comment_app.views import PostComment
from Favourite_App.models import Favourite
from Movie_Category.forms import SelectGenreFilterForm
from Movies_WebApp import settings
from Vote_app.forms import VoteForm
from Vote_app.models import Rate, Vote
from accounts.decorators import ajax_login_required
from .models import Series

class SeriesView(ListView,LoginRequiredMixin):
    template_name = 'series/series_list_view.html'
    paginate_by = settings.PAGINATE_BY
    model = Series

    def get_queryset(self):
        return Series.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(SeriesView, self).get_context_data(*args,**kwargs)
        side_filter_form = SelectGenreFilterForm(data=self.request.GET or None)
        context['side_filter_form'] = side_filter_form
        return context

class SeriesDetail(DetailView):
    template_name = 'series/series_detail_view.html'
    model = Series
    form_class = CommentForm

    def get_queryset(self):
        return Series.objects.all_with_related_persons_and_score()


    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        pk = self.kwargs['pk']
        series_obj = get_object_or_404(Series.objects.all(),series_slug=slug,pk=pk)
        ip_address = self.request.ip_address
        if ip_address not in series_obj.series_hits.all():
            series_obj.series_hits.add(ip_address)
        return series_obj


    def get_context_data(self, **kwargs):
        get_series = Series.objects.filter(pk=self.kwargs['pk']).get()
        context = super(SeriesDetail, self).get_context_data(**kwargs)
        try:
            season = [s for s in range(1,int(get_series.seasons) + 1)]
        except:
            season = 0
        context['season'] = season

        """ like or dislike """
        vote = None
        vote_form_url = None
        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                series=self.object,user=self.request.user
            )
            if vote.id:
                vote_form_url = reverse(
                    'Vote:update_vote',
                    kwargs={'obj_slug': vote.series.series_slug,
                    'obj_id': vote.series.id, 'pk': vote.id}
                )
            else:
                vote_form_url = reverse(
                    'Vote:create_vote',
                    kwargs={'obj_slug': vote.series.series_slug,
                    'obj_id': self.object.id}
                )
        vote_form = VoteForm(value=self.object.get_vote_value(request=self.request))
        context['vote_form'] = vote_form
        context['vote_form_url'] = vote_form_url
        context['vote_value'] = self.object.get_vote_value(request=self.request)


        """star rating for Series"""
        if self.request.user.is_authenticated:
            rate_object = Rate.objects.get_rate_or_unsaved_blank_rate(
                series=self.object, user=self.request.user
            )

            rate_form_url = reverse(
                'Vote:star_rate',kwargs={'obj_slug': self.object.series_slug, 'obj_id': self.object.id}
                )
            rate = 0
            if rate_object:
                rate = rate_object[0].rate
            context['review_rate'] = rate
            context['star_rate_form'] = rate_form_url

        context['rate_avg'] = Rate.objects.get_rate_avg(obj_id=self.kwargs['pk'],obj_slug=self.kwargs['slug'])

        """related Series"""

        related_series = Series.objects.filter(
            Q(genre__in=self.object.genre.all()) |
            Q(creator__series_creator=self.object)
        ).distinct().exclude(pk=self.kwargs['pk']).order_by('-release_date')

        context['related_series'] = random.sample(list(related_series),len(related_series))
        if self.request.user.is_authenticated:
            favourite_queryset = Favourite.objects.filter(
                user=self.request.user,series_id=self.object.pk,series__series_slug=self.object.series_slug
            )
            context['favourite'] = favourite_queryset

        context['comment_form'] = CommentForm()
        context['all_comments'] = CommentModel.objects.filter(series=self.get_object()).order_by('-created_on')

        return context


    def post(self, request, *args, **kwargs):
        comment = PostComment.as_view(template_name=self.template_name)
        return comment(request, *args, **kwargs)




class SeriesFilterListView(ListView):
    template_name = 'series/series_list_view.html'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self):
        return Series.objects.filter_series(filter_series=self.kwargs['filter'])


    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(SeriesFilterListView, self).get_context_data(*args, **kwargs)
        context['filter_url'] = self.kwargs['filter']
        return context