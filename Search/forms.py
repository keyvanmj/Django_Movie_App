from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label='',required=False,widget=forms.TextInput(
        attrs={'placeholder':'Search for a movie, TV Show or celebrity that you are looking for'}
    ))


