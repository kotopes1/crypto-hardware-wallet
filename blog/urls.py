""" URL patterns connecting blog """
from blog import views
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'post/<int:pk>',
        views.PostDeleteView.as_view(),
        name='comment_delete'
        ),
    path(
        'post/update<int:pk>',
        views.CommentUpdateView.as_view(),
        name='comment_update'
        ),
]
