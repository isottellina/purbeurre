# urls.py ---
#
# Filename: urls.py
# Author: Louise <louise>
# Created: Mon Apr 27 14:28:50 2020 (+0200)
# Last-Updated: Thu Apr 30 23:45:52 2020 (+0200)
#           By: Louise <louise>
#
"""
The URLs of the users app. They are divided in two groups,
basic views, that do thinks like sign-in, sign-out, and
save views, which are related to the save feature.
"""
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
