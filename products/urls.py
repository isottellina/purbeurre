# urls.py ---
#
# Filename: urls.py
# Author: Louise <louise>
# Created: Sun Apr 26 19:57:39 2020 (+0200)
# Last-Updated: Fri May  1 00:50:20 2020 (+0200)
#           By: Louise <louise>
#
"""
The URLs of the products app.
"""
from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('search', views.search, name='search'),
    path('substitute/<int:product_id>', views.substitute, name="substitute"),
    path('info/<int:product_id>', views.info, name='info')
]
