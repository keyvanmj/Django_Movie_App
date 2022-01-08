from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import FormView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from Movie_app.models import Movie
from Series_app.models import Series
from accounts.models import Profile
from .forms import CommentForm
from .models import CommentModel
from .mixins import CommentMixin

class PostComment(SingleObjectMixin, CommentMixin, FormView, LoginRequiredMixin):
    model = CommentModel
    form_class = CommentForm

    def get_object(self, queryset=None):
        try:
            qs = get_object_or_404(Movie, slug=self.kwargs['slug'], pk=self.kwargs['pk'])
        except:
            qs = get_object_or_404(Series, series_slug=self.kwargs['slug'], pk=self.kwargs['pk'])
        return qs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(PostComment, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        profile_image = None
        for p in Profile.objects.filter(user=self.request.user):
            profile_image = p

        comment = form.save(commit=False)
        try:
            comment.movie = self.object
        except:
            comment.series = self.object
        comment.user = self.request.user
        comment.image = profile_image
        comment.save()
        return super(PostComment, self).form_valid(form)


class UpdateComment(LoginRequiredMixin, CommentMixin, UpdateView):
    template_name = 'comment/update_comments.html'
    model = CommentModel
    fields = ['comment_title','content']

    def get_context_data(self, **kwargs):
        context = super(UpdateComment, self).get_context_data(**kwargs)
        update = True
        context['update'] = update
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class DeleteComment(LoginRequiredMixin, CommentMixin, DeleteView):
    template_name = 'comment/delete_comments.html'
    model = CommentModel

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

