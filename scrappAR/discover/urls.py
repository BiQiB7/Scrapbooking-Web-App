from django.contrib import admin 
from django.urls import path
from .views import discover, scrapbook

urlpatterns = [
    path('discover/',discover,name='discover'),  
    path('scrapbook/<str:pk>', scrapbook, name = 'scrapbook')
]