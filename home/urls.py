"""
The admin module in Django's contrib package is used to create
an admin interface for a Django project.
It provides a web-based interface for managing the data of a Django project.
This includes creating, reading, updating, and deleting database records,
as well as managing relationships between different models.
This module makes it easy for developers to quickly create
 an admin interface for their project, without having to build it from scratch.
:param models: The models that should be registered with the admin interface.
:type models: List[Model]
:param site_title: The title of the admin site.
:type site_title: str
:param site_header: The header of the admin site.
:type site_header: str
:return: None

"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home')
]
