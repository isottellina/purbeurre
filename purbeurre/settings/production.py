# production.py --- 
# 
# Filename: production.py
# Author: Louise <louise>
# Created: Fri May  1 01:04:57 2020 (+0200)
# Last-Updated: Thu May  7 17:44:30 2020 (+0200)
#           By: Louise <louise>
#
import os
from .base import *
from django.core.management.utils import get_random_secret_key

SECRET_KEY = os.environ.get("PURBEURRE_SECRET_KEY", get_random_secret_key())
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "purbeurre.zanier.org", "*"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB", "postgres"),
        'USER': os.environ.get("POSTGRES_USER", "postgres"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("PURBEURRE_DB_HOST", "db"),
        'PORT': os.environ.get("PURBEURRE_DB_PORT", 5432),
    }
}

STATIC_ROOT = '/static'

# Compress settings for production
# We have to compress offline because WhiteNoise won't
# service new files.
COMPRESS_ENABLED = True

# We don't need to have legible CSS in production, so
# we use the compressed output style.
LIBSASS_OUTPUT_STYLE = "compressed"
