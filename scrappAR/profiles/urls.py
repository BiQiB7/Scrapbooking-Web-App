from django.contrib import admin 
from django.urls import path
from . import views

urlpatterns = [
    # path('profile/<str:pk>',views.home,name='profile'),
    path('profile/',views.index,name='profile'),
    
]