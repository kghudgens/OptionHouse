from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('about/', views.about, name='about')
]