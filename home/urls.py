# urls.py --- 
# 
# Filename: urls.py
# Author: Louise <louise>
# Created: Sun Apr 26 21:16:25 2020 (+0200)
# Last-Updated: Mon Apr 27 00:15:10 2020 (+0200)
#           By: Louise <louise>
# 
from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('legal', views.legal, name='legal')
]
