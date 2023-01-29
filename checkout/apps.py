"""
Django's application configuration class

This class is used to configure an application and its behavior
in a Django project. It provides a way to specify
application-specific settings and customize the behavior of the application.

Attributes:
    name (str): The name of the application.
    verbose_name (str): The human-readable name of the application.

Methods:
    ready() : Method that runs when the application is ready.
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
Checkout application configuration class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
