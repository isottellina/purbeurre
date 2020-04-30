# tests.py --- 
# 
# Filename: tests.py
# Author: Louise <louise>
# Created: Tue Apr 28 00:31:16 2020 (+0200)
# Last-Updated: Thu Apr 30 23:17:08 2020 (+0200)
#           By: Louise <louise>
#
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user
from django.contrib.auth.models import User

from .. import views
from ..models import SavedProduct

class TestUserCreate(TestCase):
    USER_USERNAME = "user1"
    USER_PASSWORD = "password"
    NEW_USER_USERNAME = "user2"
    NEW_USER_PASSWORD = "password"
    
    def setUp(self):
        User.objects.create_user(
            username=self.USER_USERNAME,
            first_name='Chantal',
            email='chantal@beauregard.com',
            password=self.USER_PASSWORD
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
        self.assertEqual(
            User.objects.filter(first_name="Hélène").exists(),
            False
        )
        self.assertTemplateUsed('users/signup.html')

    def test_bad_mail(self):
        response = self.client.post('/user/signup', {
            "username": self.NEW_USER_USERNAME,
            "first_name": "Hélène",
            "email": "helene@broek",
            "password": self.NEW_USER_PASSWORD
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            User.objects.filter(first_name="Hélène").exists(),
            False
        )
        self.assertTemplateUsed('users/signup.html')

        
    def test_user_already_exists(self):
        response = self.client.post('/user/signup', {
            "username": self.USER_USERNAME,
            "first_name": "Hélène",
            "email": "helene@broek.com",
            "password": self.NEW_USER_PASSWORD
        })

        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            User.objects.filter(first_name="Hélène").exists(),
            False
        )
        self.assertTemplateUsed('users/signup.html')

    def test_user_created_successfully(self):
        response = self.client.post('/user/signup', {
            "username": self.NEW_USER_USERNAME,
            "first_name": "Hélène",
            "email": "helene@broek.com",
            "password": self.NEW_USER_PASSWORD
        })

        self.assertRedirects(response, '/')
        self.assertEqual(
            User.objects.filter(first_name="Hélène").exists(),
            True
        )

class TestUserLogin(TestCase):
    USER_USERNAME = 'user1'
    USER_PASSWORD = 'password'

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.USER_USERNAME,
            first_name='Chantal',
            email='chantal@beauregard.com',
            password=self.USER_PASSWORD
        )

    def test_get(self):
        response = self.client.get('/user/signin')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/signin.html')

    def test_login_missing_data(self):
        response = self.client.post('/user/signin', {
            "username": self.USER_USERNAME
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(get_user(self.client).is_authenticated, False)
        self.assertTemplateUsed('users/signin.html')

    def test_login_bad_data(self):
        response = self.client.post('/user/signin', {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD + "bad"
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(get_user(self.client).is_authenticated, False)
        self.assertTemplateUsed('users/signin.html')

    def test_login_success(self):
        response = self.client.post('/user/signin', {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD
        })

        self.assertRedirects(response, '/')
        self.assertEqual(get_user(self.client).is_authenticated, True)

    def test_login_success_next(self):
        response = self.client.post('/user/signin', {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD,
            "next": "/user/account"
        })

        self.assertRedirects(response, '/user/account')
        self.assertEqual(get_user(self.client).is_authenticated, True)

class TestUserLogout(TestCase):
    USER_USERNAME = 'user1'
    USER_PASSWORD = 'password'
        
    def setUp(self):
        self.user = User.objects.create_user(
            username=self.USER_USERNAME,
            first_name='Chantal',
            email='chantal@beauregard.com',
            password=self.USER_PASSWORD
        )

    def test_signout(self):
        # Sign in first
        signin_response = self.client.post("/user/signin", {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD
        })
        self.assertEqual(get_user(self.client).is_authenticated, True)

        # Then logout and check if it worked
        response = self.client.get("/user/signout")

        self.assertRedirects(response, '/')
        self.assertEqual(get_user(self.client).is_authenticated, False)

class TestUserAccount(TestCase):
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

    def test_not_logged_in(self):
        response = self.client.get("/user/account")
        
        self.assertRedirects(response, "/user/signin?next=/user/account")

    def test_success(self):
        request = self.factory.get("/user/account")
        request.user = self.user
        response = views.basic.account(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chantal")

class TestShowSaved(TestCase):
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
