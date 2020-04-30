# models.py --- 
# 
# Filename: models.py
# Author: Louise <louise>
# Created: Thu Apr 30 22:49:36 2020 (+0200)
# Last-Updated: Thu Apr 30 22:51:24 2020 (+0200)
#           By: Louise <louise>
# 
from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class SavedProduct(models.Model):
    orig_product = models.ForeignKey(Product,
                                         on_delete=models.CASCADE,
                                         related_name='original_savedproducts')
    sub_product = models.ForeignKey(Product,
                                         on_delete=models.CASCADE,
                                         related_name='replaced_savedproducts')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='saved_products')
