from django.urls import path
from .views import AjaxSearch,SearchView

app_name = 'Search'

urlpatterns = [
    path('',AjaxSearch.as_view(),name='ajax_search'),
    path('result/',SearchView.as_view(),name='search_view'),
]
