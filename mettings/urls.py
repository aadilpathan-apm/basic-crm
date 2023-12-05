from django.contrib import admin
from django.urls import path

from mettings import views

urlpatterns = [
    path('', views.index, name='mettings'),
    path('mettings', views.index, name='mettings')
]
