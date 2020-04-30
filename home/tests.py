# tests.py ---
#
# Filename: tests.py
# Author: Louise <louise>
# Created: Tue Apr 28 00:19:58 2020 (+0200)
# Last-Updated: Tue Apr 28 00:41:01 2020 (+0200)
#           By: Louise <louise>
#
from django.test import SimpleTestCase

class HomeTest(SimpleTestCase):
    def test_index(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home/index.html')

    def test_legal(self):
        response = self.client.get('/legal')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home/legal.html')
