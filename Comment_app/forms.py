from django import forms
from django.contrib.auth.models import User

from Movie_app.models import Movie
from Series_app.models import Series
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_title','content']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)
