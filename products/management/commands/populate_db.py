# populate_db.py --- 
# 
# Filename: populate_db.py
# Author: Louise <louise>
# Created: Tue Apr 28 02:32:46 2020 (+0200)
# Last-Updated: Tue Apr 28 03:27:01 2020 (+0200)
#           By: Louise <louise>
#
import requests
from products.models import Category, Product
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "Populates the database by polling from the OpenFoodFacts API"

    def add_arguments(self, parser):
        parser.add_argument('--lcode',
                            default="fr",
                            help="Language code for the OFF API")
        parser.add_argument('--ccode',
                            default="fr",
                            help="Country code for the OFF API")
        parser.add_argument('--categories',
                            type=int,
                            default=50,
                            help="Number of categories to fetch from the API.")
        parser.add_argument('--products',
                            type=int,
                            default=100,
                            help=("Maximum number of products per "
                                  "categories to fetch."))

    def clean_database(self):
        """
        Clean the database. Because of all the ON_CASCADE,
        we only need to delete all categories on all products
        should follow.
        """
        Category.objects.all().delete()
        
    def scrape_categories(self, number):
        """
        This function returns a list of `number` categories
        from the API, in the format they were given in.
        """
        url = "{endpoint}/categories.json".format(
            endpoint=self.endpoint
        )

        req = requests.get(url)
        # Only register categories within that country and with
        # more than one product (otherwise there's really no need
        # to find a substitute)
        categories = [i for i in req.json()["tags"]
                      if self.ccode + ':' in i["id"] and i["products"] > 1]
        categories = categories[:number] # We limit the number to the one given
        
        return categories

    def save_categories(self, categories):
        """
        This function saves in bulk all categories given to it.
        It usually makes only one query to the database, making
        it really fast.
        """
        Category.objects.bulk_create([
            Category(name=category['name'])
            for category in categories
        ])

    def scrape_products(self, category, number):
        """
        This function returns a list of `number` products
        from `category` category.
        """
        category_obj = Category.objects.get(name=category['name'])
        category_products = []

        print(category['name'])
        for page_nb in range(1, (category["products"] // 20) + 2):
            category_url = "{}/{}.json".format(category["url"], page_nb)
            category_page = requests.get(category_url).json()

            category_products += [
                Product(
                    name=product["product_name"],
                    url=product["url"],
                    image=product["image_url"],
                    nutriscore=product["nutrition_grade_fr"],
                    category=category_obj,

                    # Nutriments
                    energy=product.get('nutriments', {}).get('energy_100g'),
                    proteins=product.get('nutriments', {}).get('proteins_100g'),
                    fat=product.get('nutriments', {}).get('fat_100g'),
                    saturated_fat=product.get('nutriments', {}).get('saturated-fat_100g'),
                    sugar=product.get('nutriments', {}).get('sugars_100g'),
                    salt=product.get('nutriments', {}).get('salt_100g')
                )
                for product in category_page["products"]
                # We have no business with products that don't have a nutriscore
                # or even a product name, why are there products out there without
                # a product name that's beyond idiotic I can't even. Also, we remove
                # products without pictures, since we need pictures to display them.
                if ("nutrition_grade_fr" in product
                    and "product_name" in product
                    and product["product_name"]
                    and "image_url" in product
                    and product["image_url"])
            ]

            # We break if there is already enough products
            if len(category_products) >= number:
                break

        return category_products[:number]
    
    def save_products(self, products):
        """
        Same as with save_categories, this function saves
        really quickly a lot of products to DB.
        """
        Product.objects.bulk_create(products)
        
    def handle(self, **options):
        self.options = options
        self.ccode = options['ccode']
        self.endpoint = "https://{ccode}-{lcode}.openfoodfacts.org".format(
            ccode=options['ccode'],
            lcode=options['lcode']
        )

        # Clean database first
        self.clean_database()
        
        categories = self.scrape_categories(options['categories'])
        self.save_categories(categories)

        for category in categories:
            products = self.scrape_products(category, options['products'])
            self.save_products(products)
