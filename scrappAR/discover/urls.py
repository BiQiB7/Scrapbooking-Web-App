from django.contrib import admin 
from django.urls import path
from .views import DiscoverView

urlpatterns = [
    path('discover/',DiscoverView.as_view(),name='discover'),  
]