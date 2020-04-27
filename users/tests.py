# tests.py --- 
# 
# Filename: tests.py
# Author: Louise <louise>
# Created: Tue Apr 28 00:31:16 2020 (+0200)
# Last-Updated: Tue Apr 28 01:02:13 2020 (+0200)
#           By: Louise <louise>
# 
from django.test import TransactionTestCase
from django.contrib.auth.models import User

class TestUserCreate(TransactionTestCase):
    def setUp(self):
        User.objects.create(
            username='user1',
            first_name='Chantal',
            email='chantal@beauregard.com',
            password='password'
        )

    def test_get(self):
        response = self.client.get('/user/signup')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/signup.html')
        
    def test_missing_data(self):
        response = self.client.post('/user/signup', {
            "first_name": "Hélène",
            "email": "helene@broek.com"
        })

        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed('users/signup.html')

    def test_bad_mail(self):
        response = self.client.post('/user/signup', {
            "username": "user2",
            "first_name": "Hélène",
            "email": "helene@broek",
            "password": "password"
        })

        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed('users/signup.html')

        
    def test_user_already_exists(self):
        response = self.client.post('/user/signup', {
            "username": "user1",
            "first_name": "Hélène",
            "email": "helene@broek.com",
            "password": "password"
        })

        self.assertEqual(response.status_code, 409)
        self.assertTemplateUsed('users/signup.html')

    def test_user_created_successfully(self):
        response = self.client.post('/user/signup', {
            "username": "user2",
            "first_name": "Hélène",
            "email": "helene@broek.com",
            "password": "password"
        })

        self.assertRedirects(response, '/')
