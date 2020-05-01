# production.py --- 
# 
# Filename: production.py
# Author: Louise <louise>
# Created: Fri May  1 01:04:57 2020 (+0200)
# Last-Updated: Fri May  1 02:18:44 2020 (+0200)
#           By: Louise <louise>
#
import os
from .base import *

SECRET_KEY = os.environ.get("PURBEURRE_SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "louise-purbeurre.herokuapp.com"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("PURBEURRE_DB_NAME"),
        'USER': os.environ.get("PURBEURRE_DB_USER"),
        'PASSWORD': os.environ.get("PURBEURRE_DB_PASSWORD"),
        'HOST': os.environ.get("PURBEURRE_DB_HOST"),
        'PORT': os.environ.get("PURBEURRE_DB_PORT"),
    }
}

# Middleware, add WhiteNoise to it
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
