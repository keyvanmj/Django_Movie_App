from django.urls import path
from .views import SeriesView,SeriesDetail,SeriesFilterListView
app_name = 'Series'
urlpatterns = [
    path('series_list/',SeriesView.as_view(),name='series_list_view'),
    path('series_list/<str:filter>', SeriesFilterListView.as_view(), name='filter_series_list'),
    path('series_detail/<slug:slug>/<int:pk>/',SeriesDetail.as_view(),name='series_detail_view')
]