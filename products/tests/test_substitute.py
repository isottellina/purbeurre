# test_substitute.py ---
#
# Filename: test_substitute.py
# Author: Louise <louise>
# Created: Thu Apr 30 20:16:54 2020 (+0200)
# Last-Updated: Fri May  1 00:53:55 2020 (+0200)
#           By: Louise <louise>
#
"""
Tests the substitute page. We can check that the results
are there, and everything.
"""
from pathlib import Path
from django.test import TestCase

class SubstituteTest(TestCase):
    """
    The actual test case.
    """
    fixtures = [Path(__loader__.path).parent /
                "samples" /
                "sample_data.json"]

    def test_inexistent(self):
        """
        Tests an inexistent product returns a 404 page.
        """
        response = self.client.get("/product/substitute/5000")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, "products/substitute.html")

    def test_normal_product(self):
        """
        Tests a normal query.
        """
        response = self.client.get("/product/substitute/1")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/substitute.html")
        self.assertContains(response, "saucisse sèche aux noisettes")
