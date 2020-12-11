from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from User import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('optionhouseapp.urls')),
    path('register/', user_views.register, name='register'),
    path(
        'login',
        auth_views.LoginView.as_view(template_name='User/login.html'), 
        name='login'),
    path(
        'logout', 
        auth_views.LogoutView.as_view(template_name='User/logout.html'), 
        name='logout'),
]
