# test_save.py ---
#
# Filename: test_save.py
# Author: Louise <louise>
# Created: Thu Apr 30 21:39:37 2020 (+0200)
# Last-Updated: Fri May  1 00:25:19 2020 (+0200)
#           By: Louise <louise>
#
"""
Tests the views of the users app related to the saving feature.
"""
from pathlib import Path
from django.contrib.auth.models import AnonymousUser

from products.models import Product

from .helpers import UsersTestCase
from .. import views
from ..models import SavedProduct

class SaveTest(UsersTestCase):
    # We load the fixture from products
    fixtures = [Path(__loader__.path).parent.parent.parent /
                "products" /
                "tests" /
                "samples" /
                "sample_data.json"]

    def test_get_method(self):
        """
        Tests that a GET request redirects to the home page.
        """
        response = self.client.get("/user/save")

        self.assertRedirects(response, "/")

    def test_user_not_logged_in(self):
        """
        Tests that when the user is not logged in, a
        401 code is returned.
        """
        response = self.client.post("/user/save", {
            "orig_product": 1,
            "sub_product": 2
        })

        self.assertEqual(response.status_code, 401)

    def test_missing_fields(self):
        """
        Tests that if the fields are missing, a 400
        code is returned.
        """
        self.client.login(
            username=self.USER_USERNAME,
            password=self.USER_PASSWORD
        )
        response = self.client.post("/user/save")

        self.assertEqual(response.status_code, 400)

    def test_products_dont_exist(self):
        """
        Tests that if a requested product doesn't exist,
        the view returns a 404 error.
        """
        self.client.login(
            username=self.USER_USERNAME,
            password=self.USER_PASSWORD
        )
        response = self.client.post("/user/save", {
            "orig_product": 1,
            "sub_product": 5000
        })

        self.assertEqual(response.status_code, 404)

    def test_normal_query(self):
        """
        Tests that the product is saved without error
        when all parameters are good.
        """
        self.client.login(
            username=self.USER_USERNAME,
            password=self.USER_PASSWORD
        )
        response = self.client.post("/user/save", {
            "orig_product": 1,
            "sub_product": 2
        })

        self.assertEqual(response.status_code, 200)

        # The query should fail if there is more or less
        # than one saved product, and that's exactly the
        # number it should be.
        savedproduct = SavedProduct.objects.get()
        self.assertEqual(savedproduct.user, self.user)
        self.assertEqual(savedproduct.orig_product.id, 1)
        self.assertEqual(savedproduct.sub_product.id, 2)

class TestShowSaved(UsersTestCase):
    """
    Tests the page that shows the products you saved.
    """
    # We load the fixture from products here too
    fixtures = [Path(__loader__.path).parent.parent.parent /
                "products" /
                "tests" /
                "samples" /
                "sample_data.json"]

    def setUp(self):
        """
        Calls the set-up function and then adds a saved product
        to test.
        """
        super(TestShowSaved, self).setUp()

        orig_product = Product.objects.get(id=1)
        sub_product = Product.objects.get(id=2)
        self.savedproduct = SavedProduct.objects.create(
            orig_product=orig_product,
            sub_product=sub_product,
            user=self.user
        )

    def test_not_logged_in(self):
        """
        Tests that when the user is not logged in, we
        are redirected to the sign-in page.
        """
        response = self.client.get("/user/saved")

        self.assertRedirects(response, "/user/signin?next=/user/saved")
