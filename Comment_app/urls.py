from django.urls import path
from .views import UpdateComment,DeleteComment

app_name = 'Comments'
urlpatterns = [
    path('comment/<int:pk>/',UpdateComment.as_view(),name='comment_update'),
    path('comment/<int:pk>/delete/',DeleteComment.as_view(),name='comment_delete'),
]