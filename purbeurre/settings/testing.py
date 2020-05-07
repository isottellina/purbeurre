# dev.py --- 
# 
# Filename: dev.py
# Author: Louise <louise>
# Created: Sun Apr 26 13:40:52 2020 (+0200)
# Last-Updated: Thu May  7 22:45:07 2020 (+0200)
#           By: Louise <louise>
# 
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*6)v3&!@3$l9@evn*+*ec-&2o3s#fbfh&p@2fxiw3k626)q=nl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TESTING = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
