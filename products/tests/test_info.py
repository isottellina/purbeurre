# test_info.py ---
#
# Filename: test_info.py
# Author: Louise <louise>
# Created: Thu Apr 30 20:22:57 2020 (+0200)
# Last-Updated: Fri May  1 00:52:49 2020 (+0200)
#           By: Louise <louise>
#
"""
Tests the info page. This is fairly straightforward.
"""
from pathlib import Path
from django.test import TestCase

class InfoTest(TestCase):
    """
    The tests for the info page.
    """
    fixtures = [Path(__loader__.path).parent /
                "samples" /
                "sample_data.json"]

    def test_inexistent(self):
        """
        Tests an inexistent product returns a 404 page.
        """
        response = self.client.get("/product/info/5000")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, "products/info.html")

    def test_normal_product(self):
        """
        Tests a normal query.
        """
        response = self.client.get("/product/info/1")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/info.html")
        self.assertContains(response, "Énergie : 1259 kJ")
