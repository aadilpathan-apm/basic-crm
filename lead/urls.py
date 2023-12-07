from django.contrib import admin
from django.urls import path, include

from lead import views

urlpatterns = [
    path('', views.index, name='lead'),
    path('lead', views.index, name='lead')
]