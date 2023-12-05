from django.contrib import admin
from django.urls import path

from task import views

urlpatterns = [
    path('', views.index, name='task'),
    path('task', views.index, name='task')
]
