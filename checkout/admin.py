"""
This code imports the 'admin' module from the django.contrib package.
The 'admin' module provides a built-in interface for managing models
in the Django web framework.
It allows the developer to perform CRUD operations on models,
such as creating, reading, updating, and deleting, through a web interface.
It also provides a lot of other functionalities like, creating custom views,
adding custom filters, creating custom actions and many more.

"""

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
This code defines a class, 'OrderLineItemAdminInline' which subclasses 'admin.
TabularInline'.
It creates an inline admin interface for the 'OrderLineItem' model within
the Django admin interface.
This allows the developer to edit 'OrderLineItem' instances on the same page
as the parent 'Order' model.
This class can be used to customize the fields and actions that are available
for the inline model and
also to specify how the inline model should be displayed
in the admin interface.

    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
This code defines a class 'OrderAdmin' which subclasses 'admin.ModelAdmin'.
It is used to customize the Django admin interface for the 'Order' model.
This class allows the developer to specify the fields to be displayed
and their order,
customize the way the model is displayed in the admin interface,
and add custom actions and filters.
It also provide functionality to add Inline admin classes
to edit related models.

    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
