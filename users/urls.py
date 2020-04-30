# urls.py --- 
# 
# Filename: urls.py
# Author: Louise <louise>
# Created: Mon Apr 27 14:28:50 2020 (+0200)
# Last-Updated: Thu Apr 30 23:16:39 2020 (+0200)
#           By: Louise <louise>
# 
from django.urls import path

from .views import basic, save

app_name = 'users'
urlpatterns = [
    path('signup', basic.signup, name='signup'),
    path('signin', basic.signin, name='signin'),
    path('signout', basic.signout, name='signout'),
    path('account', basic.account, name='account'),

    path('save', save.save, name='save'),
    path('saved', save.show_saved, name='saved')
]
