from.views import analytics_view
from django.urls import path
urlpatterns = [
    path('analytics/', analytics_view, name='analytics'),
]