from django import forms
from django.contrib.auth.models import User

from Movie_app.models import Movie
from Series_app.models import Series
from .models import Vote, VALUE_CHOICES


class VoteForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=User.objects.all(),disabled=True
    )
    movie = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=Movie.objects.all(),
        disabled=True
    )
    series = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=Series.objects.all(),
        disabled=True
    )
    value = forms.ChoiceField(widget=forms.RadioSelect,choices=VALUE_CHOICES,required=False)

    def __init__(self,value=None):
        super(VoteForm, self).__init__()
        self.fields['value'].label = ''
        if 'LIKE' == value:
            self.fields['value'].initial = 1
        elif 'DISLIKE' == value:
            self.fields['value'].initial = -1

    class Meta:
        model = Vote
        fields = ('value','user','movie','series')