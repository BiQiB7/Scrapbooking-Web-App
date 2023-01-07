from django.urls import path, re_path
from . import views
from django.urls import re_path as url
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login')
]