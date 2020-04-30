# urls.py --- 
# 
# Filename: urls.py
# Author: Louise <louise>
# Created: Sun Apr 26 19:57:39 2020 (+0200)
# Last-Updated: Thu Apr 30 21:06:14 2020 (+0200)
#           By: Louise <louise>
# 
from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('search', views.search, name='search'),
    path('substitute/<int:product_id>', views.substitute, name="substitute"),
    path('info/<int:product_id>', views.info, name='info'),

    # Kind of API, I guess
    path('save', views.save, name='save')
]
