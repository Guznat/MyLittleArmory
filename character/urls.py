from django.contrib import admin
from django.urls import path, include
from .views import MountSearch


urlpatterns = [
    path('search/', MountSearch.as_view(), name='mounts')
]