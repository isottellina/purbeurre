<!-- README.md --- 
;; 
;; Filename: README.md
;; Author: Louise <louise>
;; Created: Mon Apr 27 01:11:58 2020 (+0200)
;; Last-Updated: Fri May  1 03:43:01 2020 (+0200)
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
## Deploying to production
To deploy the app, you can just push the repo to Heroku, with a
PostgreSQL setup. You have to set the variables :

 - PURBEURRE_SECRET_KEY
 - PURBEURRE_DB_NAME
 - PURBEURRE_DB_USER
 - PURBEURRE_DB_PASSWORD
 - PURBEURRE_DB_HOST
 - PURBEURRE_DB_PORT

Once pushed, you have to populate the database once. To do so,
just run:

```bash
heroku run DJANGO_SETTINGS_MODULE='purbeurre.settings.production' python manage.py populate_db
```

And wait for a bit.
