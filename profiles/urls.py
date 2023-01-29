"""
The path function in Django's urls module is used to define
URL patterns for a Django project.
It takes a route string and a view function or class-based view as arguments,
and maps the route to the view. When a user navigates to the specified route,
the corresponding view function is called and the resulting output
is returned to the user.
This function also supports the use of regular expressions
for more advanced URL routing.
:param route: A string defining the URL pattern.
:type route: str
:param view: The view function or class-based view that should
handle requests to the specified route.
:type view: function or class
:param kwargs: Additional keyword arguments to pass
to the view function or class-based view.
:type kwargs: dict
:return: None

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
]
