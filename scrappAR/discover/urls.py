from django.contrib import admin 
from django.urls import path
from .views import discoverView

urlpatterns = [
    path('discover/',discoverView.discover,name='discover'),  
    path('create_scrapbook/', discoverView.create_scrapbook, name='create_scrapbook'),
]