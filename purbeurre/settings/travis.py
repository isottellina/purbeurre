# testing.py --- 
# 
# Filename: testing.py
# Author: Louise <louise>
# Created: Fri May  8 16:23:32 2020 (+0200)
# Last-Updated: Fri May  8 16:26:17 2020 (+0200)
#           By: Louise <louise>
# 
import os
from .base import *
from django.core.management.utils import get_random_secret_key

SECRET_KEY = os.environ.get("PURBEURRE_SECRET_KEY", get_random_secret_key())
DEBUG = True
TESTING = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "",
        'USER': "postgres",
        'PASSWORD': "",
        'HOST': "",
        'PORT': "",
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Compress settings for production
# We have to compress offline because WhiteNoise won't
# service new files.
COMPRESS_ENABLED = True

# We don't need to have legible CSS in production, so
# we use the compressed output style.
LIBSASS_OUTPUT_STYLE = "compressed"
