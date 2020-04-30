# test_search.py --- 
# 
# Filename: test_search.py
# Author: Louise <louise>
# Created: Thu Apr 30 20:03:01 2020 (+0200)
# Last-Updated: Thu Apr 30 21:44:52 2020 (+0200)
#           By: Louise <louise>
#
from pathlib import Path
from django.test import TestCase

class SearchTest(TestCase):
    fixtures = [Path(__loader__.path).parent /
                "samples" /
                "sample_data.json"]

    def test_search_no_query(self):
        """
        Tests that the empty search page is returned when
        somebody sends an empty query.
        """
        response = self.client.get('/product/search')

        # Check that the empty search page has been rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/search.html')

    def test_search_post(self):
        """
        Tests that the search page returns the empty search
        page when a POST request is sent.
        """
        response = self.client.post('/product/search', {
            "query": "saucisson"
        })

        # Check that the empty search page has been rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/search.html')

    def test_normal_search(self):
        """
        Tests a normal search query.
        """
        response = self.client.get('/product/search', {
            "query": "saucisson"
        })

        # Check that the results page has been rendered, and
        # that a test product is really on the page.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/search_results.html')
        self.assertContains(response, "Saucisson sec Label rouge")
