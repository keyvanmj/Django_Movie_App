from django.urls import path
from .views import GenreView,SelectFilterView

app_name = 'Category'
urlpatterns = [
    path('<str:type>/<slug:hierarchy>',GenreView.as_view(),name='category_view'),
    path('list/filter/',SelectFilterView.as_view(),name='select_filter_view'),
]