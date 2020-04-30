# tests.py ---
#
# Filename: tests.py
# Author: Louise <louise>
# Created: Tue Apr 28 00:19:58 2020 (+0200)
# Last-Updated: Thu Apr 30 23:38:30 2020 (+0200)
#           By: Louise <louise>
#
"""
Tests for the home application.
"""
from django.test import SimpleTestCase

class HomeTest(SimpleTestCase):
    """All the tests."""
    def test_index(self):
        """
        Tests the index page.
        """
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home/index.html')

    def test_legal(self):
        """
        Tests the legal notices page. There is no
        worst case.
        """
        response = self.client.get('/legal')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home/legal.html')
