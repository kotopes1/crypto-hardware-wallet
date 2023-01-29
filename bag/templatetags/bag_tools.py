"""
The template module in Django provides a framework for defining and using
templates in a Django application.
The template module includes a variety of tools for working with templates,
such as the `Template` class and the `Context` class.
These can be used to load and render templates, as well as to pass data to
templates for use in rendering.
To use the template module, you will need to import it and create
an instance of the
`Template` class. You can then use this instance to render the template
with a given context.
The template also allows to use custom tags and filters.
"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
Calculate the subtotal of a given order.
The function takes a list of items, where each item is a dictionary
that includes the name, quantity,
and price of the item, and returns the subtotal of the order.
The function performs the calculation by iterating over the items,
multiplying the quantity by the price for each item, and summing the results.
:param items: list of dictionaries containing item information
:type items: list
:return: the subtotal of the order
:rtype: float
"""
    return price * quantity
