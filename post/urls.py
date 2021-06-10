from post.models import Post
from django.urls import path
from . import views


urlpatterns=[
    path('',views.PostListView.as_view(),name='list_post'),
    path('post/<slug:slug>', views.PostDetailView.as_view()),
    path('post/new/',views.PostNewView.as_view(),name='new_post'),
    path('post/<slug:slug>/edit',views.PostUpdateViews.as_view()),
]