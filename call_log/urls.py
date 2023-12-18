from django.contrib import admin
from django.urls import path

from call_log import views

urlpatterns = [
    path('', views.index, name='call_log/'),
    path('call_log/', views.index, name='call_log/'),
    path('add_modal/', views.add_modal, name='add_modal'),
    path('add/', views.add, name='add'),
    path('edit_modal/<uuid:uuid>/', views.edit_modal, name='edit_modal'),
    path('edit/<uuid:uuid>/', views.edit, name='edit'),
    path('delete_modal/<uuid:uuid>/', views.delete_modal, name='delete_modal'),
    path('delete/<uuid:uuid>/', views.delete, name='delete'),
]