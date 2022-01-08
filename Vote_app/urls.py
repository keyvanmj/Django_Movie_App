from django.urls import path
from .views import CreateVote,UpdateVote,create_rate,RateView


app_name = 'Vote'
urlpatterns = [
    path('movie/<str:obj_slug>/<int:obj_id>/voted',CreateVote.as_view(),name='create_vote'),
    path('movie/<str:obj_slug>/<int:obj_id>/voted/<int:pk>',UpdateVote.as_view(),name='update_vote'),
    path('movie&series/<str:obj_slug>/<int:obj_id>/rated',create_rate,name='star_rate'),
    path('rated/list',RateView.as_view(),name='rate_list_view')
]
