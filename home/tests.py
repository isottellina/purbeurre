# tests.py --- 
# 
# Filename: tests.py
# Author: Louise <louise>
# Created: Tue Apr 28 00:19:58 2020 (+0200)
# Last-Updated: Tue Apr 28 00:23:31 2020 (+0200)
#           By: Louise <louise>
# 
from django.test import TestCase
from django.test import Client

class HomeTest(TestCase):
    def test_index(self):
        client = Client()
        response = client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_legal(self):
        client = Client()
        response = client.get('/legal')

        self.assertEqual(response.status_code, 200)
