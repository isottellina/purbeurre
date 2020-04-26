# urls.py --- 
# 
# Filename: urls.py
# Author: Louise <louise>
# Created: Sun Apr 26 19:57:39 2020 (+0200)
# Last-Updated: Sun Apr 26 19:57:56 2020 (+0200)
#           By: Louise <louise>
# 
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
