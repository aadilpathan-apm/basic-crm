"""
URL configuration for basic_crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Basic CRM"
admin.site.site_title = "Basic CRM Admin Portal"
admin.site.index_title = "Welcome to Basic CRM Admin Portal"

urlpatterns = [
    path('', include('home.urls')),
    path('home', include('home.urls')),
    path('task', include('task.urls')),
    path('customers', include('customers.urls')),
    path('notes', include('notes.urls')),
    path('calls/', include('calls.urls')),
    path('mettings', include('mettings.urls')),
    path('appointments', include('appointments.urls')),
    path('admin/', admin.site.urls),
]
