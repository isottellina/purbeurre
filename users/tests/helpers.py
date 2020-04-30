# helpers.py ---
#
# Filename: helpers.py
# Author: Louise <louise>
# Created: Thu Apr 30 23:56:01 2020 (+0200)
# Last-Updated: Fri May  1 00:01:22 2020 (+0200)
#           By: Louise <louise>
#
"""
Defines helpers for the tests of the users app.
"""
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

class UsersTestCase(TestCase):
    """
    A helper class for test cases to inherit.
    It sets up an user and a RequestFactory.
    """
    USER_USERNAME = "user1"
    USER_PASSWORD = "password"

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username=self.USER_USERNAME,
            first_name='Chantal',
            email='chantal@beauregard.com',
            password=self.USER_PASSWORD
        )
