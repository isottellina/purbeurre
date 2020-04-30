# test_save.py --- 
# 
# Filename: test_save.py
# Author: Louise <louise>
# Created: Thu Apr 30 21:39:37 2020 (+0200)
# Last-Updated: Thu Apr 30 23:14:39 2020 (+0200)
#           By: Louise <louise>
# 
from pathlib import Path
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User

from .. import views
from ..models import SavedProduct

class SaveTest(TestCase):
    USER_USERNAME = "user1"
    USER_PASSWORD = "password"

    # We load the fixture from products
    fixtures = [Path(__loader__.path).parent.parent.parent /
                "products" /
                "tests" /
                "samples" /
                "sample_data.json"]

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username=self.USER_USERNAME,
            first_name="Chantal",
            email="chantal@beauregard.com",
            password=self.USER_PASSWORD
        )
    
    def test_get_method(self):
        """
        Tests that a GET request redirects to the home page.
        """
        response = self.client.get("/product/save")

        self.assertRedirects(response, "/")

    def test_user_not_logged_in(self):
        """
        Tests that when the user is not logged in, a
        401 code is returned.
        """
        request = self.factory.post("/product/save", {
            "orig_product": 1,
            "sub_product": 2
        })
        request.user = AnonymousUser()
        response = views.save.save(request)

        self.assertEqual(response.status_code, 401)

    def test_missing_fields(self):
        """
        Tests that if the fields are missing, a 400
        code is returned.
        """
        request = self.factory.post("/product/save")
        request.user = self.user
        response = views.save.save(request)
        
        self.assertEqual(response.status_code, 400)

    def test_products_dont_exist(self):
        """
        Tests that if a requested product doesn't exist,
        the view returns a 404 error.
        """
        request = self.factory.post("/product/save", {
            "orig_product": 1,
            "sub_product": 5000
        })
        request.user = self.user
        response = views.save.save(request)

        self.assertEqual(response.status_code, 404)

    def test_normal_query(self):
        """
        Tests that the product is saved without error
        when all parameters are good.
        """
        request = self.factory.post("/product/save", {
            "orig_product": 1,
            "sub_product": 2
        })
        request.user = self.user
        response = views.save.save(request)

        self.assertEqual(response.status_code, 200)

        # The query should fail if there is more or less
        # than one saved product, and that's exactly the
        # number it should be.
        savedproduct = SavedProduct.objects.get()
        self.assertEqual(savedproduct.user, self.user)
        self.assertEqual(savedproduct.orig_product.id, 1)
        self.assertEqual(savedproduct.sub_product.id, 2)
