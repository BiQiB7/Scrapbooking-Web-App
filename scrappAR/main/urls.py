from django.urls import path, re_path
from . import views
from django.urls import re_path as url
urlpatterns = [
    path('', views.home, name='home')
]