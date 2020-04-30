# admin.py ---
#
# Filename: admin.py
# Author: Louise <louise>
# Created: Thu Apr 30 23:41:40 2020 (+0200)
# Last-Updated: Thu Apr 30 23:42:59 2020 (+0200)
#           By: Louise <louise>
#
"""
Register the only model in the app to the admin interface.
"""
from django.contrib import admin
from . import models

admin.site.register(models.SavedProduct)
