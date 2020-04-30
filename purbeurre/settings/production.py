# production.py --- 
# 
# Filename: production.py
# Author: Louise <louise>
# Created: Fri May  1 01:04:57 2020 (+0200)
# Last-Updated: Fri May  1 01:23:44 2020 (+0200)
#           By: Louise <louise>
#
import os
from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Middleware, add WhiteNoise to it
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
