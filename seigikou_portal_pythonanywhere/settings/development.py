from os import environ
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0%_)ieqicu%11yq&zcrjdi)e@51nj)v)or^cth+5r5(v5u1b6@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] 

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {    
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }    
}
"""
DATABASES = {    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME'  :  'mysql_testdb',
        'USER'  :'root',
        'PASSWORD':'root',
        'HOST'  :'127.0.0.1',
        'POST'  :'3306',
    }    
}
"""
AUTH_PASSWORD_VALIDATORS = []
