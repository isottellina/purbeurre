# urls.py --- 
# 
# Filename: urls.py
# Author: Louise <louise>
# Created: Sun Apr 26 19:57:39 2020 (+0200)
# Last-Updated: Tue Apr 28 20:12:53 2020 (+0200)
#           By: Louise <louise>
# 
from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('search/', views.search, name='search'),
]
