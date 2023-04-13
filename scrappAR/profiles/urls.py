from django.contrib import admin 
from django.urls import path
from . import views
from .views import ProfileView

urlpatterns = [
    # path('profile/<str:pk>',views.home,name='profile'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    
    
]