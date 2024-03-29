"""scrappAR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
import profiles.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include(('users.urls','users'),namespace = 'users')),
    path('', include(('profiles.urls','profile'),namespace = 'profile')),
    path('', include(('discover.urls','discover'),namespace = 'discover')),
    path('', include(('scrapbook.urls','scrapbook'),namespace = 'scrapbook')),
    path('', include(('analytics.urls','analytics'),namespace = 'analytics')),
    # path('', include(('camera.urls','camera'),namespace='camera')),
    # path('profile/', views.home,namespace='home'),
    # path('', include(('profiles.urls','home'),namespace = 'home')),
    # path('scrapbook/', include('scrapbook.urls')),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)