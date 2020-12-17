from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('postlist/', views.PostListView.as_view(), name='post-list' ),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post-create', views.CreatePostView.as_view(), name='post_form')

]