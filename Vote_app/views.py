from itertools import chain

from Movie_app.models import Movie
from Series_app.models import Series
from .mixins import VoteMixin
from django.db.models import Q
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView, FormView, ListView
from Vote_app.forms import VoteForm
from Vote_app.models import Vote, Rate
from accounts.decorators import ajax_login_required


class CreateVote(VoteMixin,LoginRequiredMixin, CreateView):
    form_class = VoteForm

    def post(self, request, *args, **kwargs):

        vote_obj = [x.value for x in self.combine_vote_obj()]
        vote_value = request.POST.get('vote_data')
        if not vote_obj:
            try:
                vote = Vote(
                    movie=self.get_object(),
                    value=vote_value,
                    user=request.user, ip_address=self.request.user.ip_address).save()
                v_obj = Vote.objects.get_vote_or_unsaved_blank_vote(
                    movie=self.get_object(),
                    user=self.request.user
                )
            except:
                vote = Vote(
                    series=self.get_object(),
                    value=vote_value,
                    user=request.user, ip_address=self.request.user.ip_address).save()

                v_obj = Vote.objects.get_vote_or_unsaved_blank_vote(
                    series=self.get_object(),
                    user=self.request.user
                )
            if request.is_ajax():
                if v_obj.movie != None:
                    vote_form_url = reverse(
                        'Vote:create_vote', kwargs={'obj_slug': v_obj.movie.slug, 'obj_id': v_obj.movie.id}
                    )
                else:
                    vote_form_url = reverse(
                        'Vote:create_vote', kwargs={'obj_slug': v_obj.series.series_slug, 'obj_id': v_obj.series.pk}
                    )
                vote_status = None
                items = []
                for i in self.combine_movie_series_qs():
                    items.append(i.get_vote_value(request=request))
                vote_status = items
                data = {
                    'vote_status': vote_status,
                    'create_vote_url': vote_form_url
                }
                return JsonResponse(data)
        # return super(CreateVote, self).post(request, *args, **kwargs)


class UpdateVote(VoteMixin,LoginRequiredMixin, UpdateView):
    form_class = VoteForm

    def post(self, request, *args, **kwargs):
        vote_obj = [x.value for x in self.combine_vote_obj()]
        vote_value = request.POST.get('vote_data')
        if vote_obj:
            self.combine_vote_obj().update(value=vote_value)

            if request.is_ajax:
                vote_status = None
                items = []
                for i in self.combine_movie_series_qs():
                    items.append(i.get_vote_value(request=request))
                vote_status = items
                data = {
                    'vote_status': vote_status
                }
                return JsonResponse(data)
        return super(UpdateVote, self).post(request, *args, **kwargs)

def save_rate(request,object_id,value,object_slug=None):
    movie = Movie.objects.filter(slug=object_slug)
    series = Series.objects.filter(series_slug=object_slug)
    if movie:
        rate = Rate(
            movie_id=object_id, rate=value, user=request.user).save()
    elif series:
        rate = Rate(
            series_id=object_id, rate=value, user=request.user).save()
    else:
        return redirect('Main:home')
    return rate



@ajax_login_required
def create_rate(request, obj_id=None, obj_slug=None):
    val_ = request.POST.get('val_')

    if request.user.is_authenticated:
        rate = Rate.objects.filter(
            (Q(movie_id=obj_id) & Q(movie__slug=obj_slug)) |
            (Q(series_id=obj_id) & Q(series__series_slug=obj_slug)),
            user=request.user)

        if not rate.exists():
            save_rate(request,object_id=obj_id,value=val_,object_slug=obj_slug)
        else:
            Rate.objects.filter(
                (Q(movie_id=obj_id) & Q(movie__slug=obj_slug)) |
                (Q(series_id=obj_id) & Q(series__series_slug=obj_slug)),
                user=request.user).update(rate=val_)

    else:
        return redirect('Main:home')

    if request.is_ajax():

        rate_avg = Rate.objects.get_rate_avg(obj_id=obj_id,obj_slug=obj_slug)
        rated = Rate.objects.all()
        r = None
        if rated.exists():
            r = 'True'
        else:
            r = 'False'
        data = {
            'rate_data': rate_avg,
            'rated': r,
        }
        return JsonResponse(data)



    return redirect(request.META['HTTP_REFERER'])


class RateView(ListView, LoginRequiredMixin):
    template_name = 'rate_list_view.html'
    paginate_by = 5

    @method_decorator(ajax_login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super(RateView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        rate = Rate.objects.filter(user=self.request.user).order_by('-rate','-rate_on')
        chained_rate_obj = list((x.movie, x.series) for x in rate)
        chained_items = [x for x in chained_rate_obj for x in x]
        all_obj = list(filter(None, chained_items))
        return all_obj

    def get_context_data(self, *args, **kwargs):
        context = super(RateView, self).get_context_data(*args,**kwargs)
        context['objects_count'] = self.object_list.__len__()
        context['queryset_objects'] = [s.get_obj_model_name for s in self.object_list]
        return context
