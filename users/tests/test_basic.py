# tests.py ---
#
# Filename: tests.py
# Author: Louise <louise>
# Created: Tue Apr 28 00:31:16 2020 (+0200)
# Last-Updated: Fri May  1 00:27:56 2020 (+0200)
#           By: Louise <louise>
#
"""
Tests the basic views of the users app.
"""
from django.contrib.auth import get_user
from django.contrib.auth.models import User

from .helpers import UsersTestCase

class TestUserCreate(UsersTestCase):
    """
    Tests the sign-up view, related to the
    creation of an user.
    """
    NEW_USER_USERNAME = "user2"
    NEW_USER_PASSWORD = "password"

    def test_get(self):
        """
        When we send a GET request, we should be redirected
        to the home page.
        """
        response = self.client.get('/user/signup')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/signup.html')

    def test_missing_data(self):
        """
        If there is data missing from the form, we
        should get a HTTP 400.
        """
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
        """
        If the e-mail is not a correct one, we should get
        HTTP 400 too.
        """
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
        """
        If the user already exists, we should get a HTTP 409.
        This is only determined by the username.
        """
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
        """
        If all data is well-formed, the user should be created,
        and we should be redirected to the home page.
        """
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

class TestUserLogin(UsersTestCase):
    """
    Tests the view related to log-in.
    """
    def test_get(self):
        """
        When we send a GET request, we should get
        the form.
        """
        response = self.client.get('/user/signin')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/signin.html')

    def test_login_missing_data(self):
        """
        In the case of missing data, we should get
        a HTTP 400.
        """
        response = self.client.post('/user/signin', {
            "username": self.USER_USERNAME
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(get_user(self.client).is_authenticated, False)
        self.assertTemplateUsed('users/signin.html')

    def test_login_bad_data(self):
        """
        If one of the two fields is incorrect, we should
        get a HTTP 400.
        """
        response = self.client.post('/user/signin', {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD + "bad"
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(get_user(self.client).is_authenticated, False)
        self.assertTemplateUsed('users/signin.html')

    def test_login_success(self):
        """
        If all info is good, we should be redirected
        and be logged in.
        """
        response = self.client.post('/user/signin', {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD
        })

        self.assertRedirects(response, '/')
        self.assertEqual(get_user(self.client).is_authenticated, True)

    def test_login_success_next(self):
        """
        If we came to the page with a next parameter, even
        in post, we should be redirected to the page specified.
        """
        response = self.client.post('/user/signin', {
            "username": self.USER_USERNAME,
            "password": self.USER_PASSWORD,
            "next": "/user/account"
        })

        self.assertRedirects(response, '/user/account')
        self.assertEqual(get_user(self.client).is_authenticated, True)

class TestUserLogout(UsersTestCase):
    """
    Tests the logout page.
    """
    def test_signout(self):
        """
        Tests the log out per se.
        """
        # First log-in.
        self.client.login(
            username=self.USER_USERNAME,
            password=self.USER_PASSWORD
        )
        self.assertEqual(get_user(self.client).is_authenticated, True)

        # Then logout and check if it worked
        response = self.client.get("/user/signout")

        self.assertRedirects(response, '/')
        self.assertEqual(get_user(self.client).is_authenticated, False)

class TestUserAccount(UsersTestCase):
    """
    Tests the account page.
    """
    def test_not_logged_in(self):
        """
        If we're not logged in, we should be redirected.
        """
        response = self.client.get("/user/account")

        self.assertRedirects(response, "/user/signin?next=/user/account")

    def test_success(self):
        """
        If we're logged in, we should get to the account
        page and it should be our own.
        """
        self.client.login(
            username=self.USER_USERNAME,
            password=self.USER_PASSWORD
        )
        response = self.client.get("/user/account")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chantal")
