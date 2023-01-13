from django.urls import path, include
from users import views as usersview
from main import views as mainview
from django.urls import re_path as url
urlpatterns = [
    path('', mainview.home, name='home'),
    path('login/', usersview.user_login, name='login'),
    path('register/', usersview.user_registration, name='register')
]