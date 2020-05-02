# models.py ---
#
# Filename: models.py
# Author: Louise <louise>
# Created: Tue Apr 28 01:56:27 2020 (+0200)
# Last-Updated: Sat May  2 22:31:58 2020 (+0200)
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
    name = models.CharField(max_length=100, unique=True)

class Product(models.Model):
    """
    This is a product. It contains every information we
    need for the system to function, and a bit more to
    display them in the info page.

    The product is identified (other than by its PK) by
    its URL, to avoid adding twice the same product.
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

    class Meta:
        """
        We identify a product by its URL being unique. But
        one product can be several times in the database,
        being that they can be in different categories.
        Thus, we set a constraint for only one product
        having a distinct URL in one category
        """
        constraints = [
            models.UniqueConstraint(fields=["url", "category"],
                                    name="each_product_exists_only_once")
        ]
