from django.contrib import admin
from django.urls import path

from customers import views

urlpatterns = [
    path('', views.index, name='customers'),
    path('customers', views.index, name='customers')
]
