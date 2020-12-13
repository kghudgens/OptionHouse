from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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
    path('profile/', user_views.profile, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, )