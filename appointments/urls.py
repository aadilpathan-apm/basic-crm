from django.contrib import admin
from django.urls import path

from appointments import views

urlpatterns = [
    path('', views.index, name='appointments'),
    path('appointments', views.index, name='appointments')
]
