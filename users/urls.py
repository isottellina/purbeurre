# urls.py --- 
# 
# Filename: urls.py
# Author: Louise <louise>
# Created: Mon Apr 27 14:28:50 2020 (+0200)
# Last-Updated: Mon Apr 27 14:29:13 2020 (+0200)
#           By: Louise <louise>
# 
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('signup', views.signup, name='signup'),
]
