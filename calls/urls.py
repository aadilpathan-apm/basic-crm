from django.contrib import admin
from django.urls import path

from calls import views

urlpatterns = [
    path('', views.index, name='calls'),
    path('calls', views.index, name='calls'),
    path('add_modal/', views.add_modal, name='add_modal'),
    path('edit_modal/', views.edit_modal, name='edit_modal'),
    path('delete_modal/', views.delete_modal, name='delete_modal'),
]
