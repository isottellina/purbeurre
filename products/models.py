# models.py ---
#
# Filename: models.py
# Author: Louise <louise>
# Created: Tue Apr 28 01:56:27 2020 (+0200)
# Last-Updated: Fri May  1 00:38:50 2020 (+0200)
#           By: Louise <louise>
#
"""
The models of the products app.
"""
from django.db import models

class Category(models.Model):
    """
    This is a category. It has a one-to-many relationship
    with Product.
    """
    name = models.CharField(max_length=100)

class Product(models.Model):
    """
    This is a product. It contains every information we
    need for the system to function, and a bit more to
    display them in the info page.
    """
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=368)
    image = models.URLField(max_length=368)
    nutriscore = models.CharField(max_length=1)

    energy = models.DecimalField(max_digits=9,
                                 decimal_places=4,
                                 null=True)
    proteins = models.DecimalField(max_digits=7,
                                   decimal_places=4,
                                   null=True)
    fat = models.DecimalField(max_digits=7,
                              decimal_places=4,
                              null=True)
    saturated_fat = models.DecimalField(max_digits=7,
                                        decimal_places=4,
                                        null=True)
    sugar = models.DecimalField(max_digits=7,
                                decimal_places=4,
                                null=True)
    salt = models.DecimalField(max_digits=7,
                               decimal_places=4,
                               null=True)

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products')
