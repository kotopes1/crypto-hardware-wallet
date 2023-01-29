"""
The path function in Django's urls module is used to define URL patterns for a
Django application.
The path function takes a string pattern and a view function as arguments,
and maps the pattern to the view function. When a user requests a URL
that matches the pattern,
the view function is called to handle the request.
The path function also allows you to include optional capture groups
in the pattern,
which can be passed as arguments to the view function.
To use the path function, you will need to import it and use it to define
the URL patterns for your application in the urls.py file.
This function is useful to map the URLs to the views and to handle
the requests and responses.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),
]
