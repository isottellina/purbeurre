# test_populate.py --- 
# 
# Filename: test_populate.py
# Author: Louise <louise>
# Created: Tue Apr 28 17:18:57 2020 (+0200)
# Last-Updated: Tue Apr 28 19:42:52 2020 (+0200)
#           By: Louise <louise>
#
import json
from pathlib import Path
from django.test import TransactionTestCase
from django.core import management
from unittest.mock import patch

from products.management.commands.populate_db import Command as PopulateCommand
from products.models import Category, Product

class DummyResponse():
    """
    A dummy response to mock requests.get.
    Init it with the filename of the JSON
    file you want it to respond with.
    """
    def __init__(self, filename):
        self.filename = filename
    def json(self):
        """
        Returns with the content of the JSON file.
        """
        with open(self.filename) as file:
            return json.load(file)

class TestScrape(TransactionTestCase):
    def setUp(self):
        pass

    @patch('requests.get')
    def test_scrape_categories(self, mock_request):
        mock_request.return_value = DummyResponse(
            Path(__loader__.path).parent /
            "samples" /
            "openfoodfacts_categories.json"
        )
        
        # Init the command object
        command = PopulateCommand()
        command.endpoint = "https://fr-fr.openfoodfacts.org"
        command.ccode = "fr"
        categories = command.scrape_categories(2)
        
        # Check if the categories are those that should be and
        # not those that should be ignored.
        self.assertEqual(categories[0]['name'], "Saucissons")
        self.assertEqual(categories[1]['name'], "Comté")
        
        # Check the requests.get function has been well-used
        mock_request.assert_called_once_with(
            "https://fr-fr.openfoodfacts.org/categories.json"
        )

    @patch('requests.get')
    def test_scrape_products(self, mock_request):
        with open(Path(__loader__.path).parent /
                  "samples" /
                  "openfoodfacts_one_category.json") as file:
            categories = json.load(file)
        
        mock_request.return_value = DummyResponse(
            Path(__loader__.path).parent /
            "samples" /
            "openfoodfacts_saucissons.json"
        )

        # Init the command object
        command = PopulateCommand()
        # Save the categories
        command.save_categories(categories)
        # Scrape the actual products
        products = command.scrape_products(categories[0], 2)
        
        # Check if the product are those that should be.
        self.assertEqual(products["products"][0]['name'], "Saucisson sec pur porc label rouge")
        self.assertEqual(products["products"][1]['name'], "Saucisson sec")
        
        # Check the requests.get function has been well-used
        mock_request.assert_called_once_with(
            "https://fr.openfoodfacts.org/categorie/saucissons/1.json"
        )

class TestClean(TransactionTestCase):
    def setUp(self):
        management.call_command("loaddata",
                                (Path(__loader__.path).parent /
                                 "samples" /
                                 "sample_data.json"),
                                verbosity=0)

    def test_clean_database(self):
        # Check that there is indeed 2 categories and 10 products
        self.assertEqual(Category.objects.all().count(), 2)
        self.assertEqual(Product.objects.all().count(), 10)

        # Clean database
        command = PopulateCommand()
        command.clean_database()

        # Check the database is now empty
        self.assertEqual(Category.objects.all().count(), 0)
        self.assertEqual(Product.objects.all().count(), 0)

class TestCommand(TransactionTestCase):
    @patch('products.management.commands.populate_db.Command.scrape_categories')
    @patch('products.management.commands.populate_db.Command.scrape_products')
    def test_handle(self, mock_products, mock_categories):
        with open(Path(__loader__.path).parent /
                  "samples" /
                  "openfoodfacts_one_category.json") as file:
            mock_categories.return_value = json.load(file)
        with open(Path(__loader__.path).parent /
                  "samples" /
                  "openfoodfacts_two_products.json") as file:
            mock_products.return_value = json.load(file)

        management.call_command("populate_db", categories=1, products=2)

        # Assert there are enough records in the DB
        self.assertEqual(Category.objects.all().count(), 1)
        self.assertEqual(Product.objects.all().count(), 2)
