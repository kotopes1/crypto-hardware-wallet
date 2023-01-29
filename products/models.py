"""
A simple model representing an object with a name and a description.

Attributes:
name (str): The name of the object.
description (str): A short description of the object.
"""

from django.db import models


class Category(models.Model):
    """
    A class representing a category of items.
    Attributes:
        name (str): The name of the category.
        description (str): A short description of the category.
        items (List[Item]): A list of items that belong to this category.
        Methods:
        add_item(item: Item): Add an item to the category.
        remove_item(item: Item): Remove an item from the category.
    """

    class Meta:
        """
        A class containing metadata for a model.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns a friendly version of the input name.
        Args:
        name (str): The name to be converted.
        Returns:
        str: The friendly version of the input name.
        """
        return self.friendly_name


class Product(models.Model):
    """
    A class representing a product.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        in_stock (bool): Indicates whether the product is in stock.
        category (str): The category of the product.
        """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
