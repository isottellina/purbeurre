# admin.py ---
#
# Filename: admin.py
# Author: Louise <louise>
# Created: Fri May  1 00:30:49 2020 (+0200)
# Last-Updated: Fri May  1 00:31:16 2020 (+0200)
#           By: Louise <louise>
# 
from django.contrib import admin

from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
