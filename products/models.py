# models.py --- 
# 
# Filename: models.py
# Author: Louise <louise>
# Created: Tue Apr 28 01:56:27 2020 (+0200)
# Last-Updated: Tue Apr 28 03:06:56 2020 (+0200)
#           By: Louise <louise>
#
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=368)
    image = models.URLField(max_length=368)
    nutriscore = models.CharField(max_length=1)

    energy = models.DecimalField(max_digits=7,
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

class SavedProduct(models.Model):
    original_product = models.ForeignKey(Product,
                                         on_delete=models.CASCADE,
                                         related_name='original_savedproducts')
    replaced_product = models.ForeignKey(Product,
                                         on_delete=models.CASCADE,
                                         related_name='replaced_savedproducts')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='saved_products')
