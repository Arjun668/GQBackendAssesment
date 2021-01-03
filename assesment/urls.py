from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

from . import views
from .views import *
from assesment.forms import LoginForm


app_name = "assesment"

urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(form_class=LoginForm, template_name='assesment/login.html'),
         name='login'),

    path('', auth_views.LoginView.as_view(form_class=LoginForm, template_name='assesment/login.html'),
         name='loginpage'),


    path('logout/', CustomLogout.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

]