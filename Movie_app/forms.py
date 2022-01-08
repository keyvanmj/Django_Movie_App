from django import forms
from django.contrib.auth.models import User

from .models import MovieImage,Movie



class MovieImageForm(forms.ModelForm):
    movie = forms.ModelChoiceField(widget=forms.HiddenInput,
    queryset=Movie.objects.all(),disabled=True
    )
    user = forms.ModelChoiceField(widget=forms.HiddenInput,
    queryset=User.objects.all(),disabled=True
    )
    class Meta:
        model = MovieImage
        fields = ('image','user','movie',)

