<!-- README.md --- 
;; 
;; Filename: README.md
;; Author: Louise <louise>
;; Created: Mon Apr 27 01:11:58 2020 (+0200)
;; Last-Updated: Tue Apr 28 19:55:30 2020 (+0200)
;;           By: Louise <louise>
 -->
# Pur beurre
Pur beurre is a (fake) company in France. This is the repo for their
website. It can be used to find substitutes for a product, using data
from OpenFoodFacts.

## Setting up
You just have to set up a virtual env and install the requirements.

```bash
virtualenv -p python3 env && . env/bin/activate
pip install -r requirements.txt
```

Once set up, you have to populate the database, and before that,
you have to ensure that data migrations have been applied.

```bash
python3 manage.py migrate
python3 manage.py populate_db
```

By default, this will populate with 50 categories and at most 100
products by category. You can change this with the `--categories`
and `--products` options.

## Running the dev server
To run the dev server, you can just run it using the manage script:

```bash
python3 manage.py runserver
```
