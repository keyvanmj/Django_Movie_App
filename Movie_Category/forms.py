import json
from itertools import chain
from django import forms
from django.urls import reverse

from .models import Genre
from Movie_app.models import Movie
from Series_app.models import Series


class SelectGenreFilterForm(forms.ModelForm):

    type_select = None
    release_date = None
    genre_queryset = Genre.objects.all()
    genres = [g.title for g in genre_queryset]

    genre_select = forms.ChoiceField(
        choices=([genre, genre] for genre in genres), required=False
    )

    class Meta:
        model = Genre
        fields = ['genre_select']

    def __init__(self,data,*args,**kwargs):
        super(SelectGenreFilterForm, self).__init__(data,args,kwargs)
        movies_query = Movie.objects.all()
        series_query = Series.objects.all()
        merge_models = list(chain(movies_query.distinct('types'), series_query.distinct('types')))
        m_release_obj = [r.release_date for r in movies_query.distinct('release_date')]
        s_release_obj = [r.release_date for r in series_query.distinct('release_date')]
        merge_release_date = list(chain(m_release_obj,s_release_obj))
        sorted_merge_release_date = sorted(merge_release_date,key=lambda x:(len(x),x))
        self.fields['type_select'] = forms.ChoiceField(
            choices=([type_.types, type_.types] for type_ in merge_models), required=False
        )

        self.fields['release_date'] = forms.ChoiceField(
            choices=([r_d, r_d] for r_d in sorted_merge_release_date), required=False, label='Release Date'
        )

        self.fields['type_select'].choices.insert(0,[('All'),('All')])
        self.Meta.fields += 'type_select','release_date'

