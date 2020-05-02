# models.py ---
#
# Filename: models.py
# Author: Louise <louise>
# Created: Thu Apr 30 22:49:36 2020 (+0200)
# Last-Updated: Sat May  2 21:41:22 2020 (+0200)
#           By: Louise <louise>
#
"""
Register the only model in the app, SavedProduct.
"""
from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class SavedProduct(models.Model):
    """
    SavedProduct maps a user to several products
    that were found by the search engine to be
    substitutes.
    """
    orig_product = models.ForeignKey(Product,
                                     on_delete=models.CASCADE,
                                     related_name='original_savedproducts')
    sub_product = models.ForeignKey(Product,
                                    on_delete=models.CASCADE,
                                    related_name='replaced_savedproducts')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='saved_products')

    class Meta:
        """
        Add constraints to guarantee uniqueness of user and sub_product.
        By that, I mean that a given user can save onle one time a sub_product.
        """
        constraints = [
            models.UniqueConstraint(fields=["user", "sub_product"],
                                    name="each_product_saved_only_once")
        ]
