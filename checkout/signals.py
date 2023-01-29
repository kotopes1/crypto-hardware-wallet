"""
The post_save and post_delete signals in Django provide a way
to perform actions
after a model's save() or delete() methods are called.
The post_save signal is sent after an object is saved to the database,
and the post_delete signal is sent after an object is deleted
from the database.
To use these signals, you will need to import them and connect them
to a receiver function.
The receiver function will be called with the sender model and the instance
of the saved or deleted
object as arguments.These signals allows developers to perform additional
tasks and customizations on the models,
such as sending notifications, updating other models, and more.
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
