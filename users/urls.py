from os import name
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'users'

urlpatterns = [
    path('home/', views.home.as_view(), name='home'),
    path('register', views.register, name='register'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile.as_view(), name='user-profile'),


]