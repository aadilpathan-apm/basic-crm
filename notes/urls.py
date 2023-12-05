from django.contrib import admin
from django.urls import path

from notes import views

urlpatterns = [
    path('', views.index, name='notes'),
    path('notes', views.index, name='notes')
]
