from django.urls import path, include
from .views import *

app_name = 'blog'
urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('all/', PostListView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
    path('comment/create/', CommentCreateView.as_view())
]
