
from django import template
from Search.forms import SearchForm

register = template.Library()

@register.inclusion_tag('search/search_tag.html')
def search_tag(request):
    form = SearchForm(request.GET)
    # results = None
    if 'q' in request.GET:
        if form.is_valid():
            q = form.cleaned_data.get('q')
            # results = Movie.objects.search_movies(q)


    context = {
        'form':form,
        # 'results':results,
    }
    return context
