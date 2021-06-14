from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['saberproufps.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd4m72co4s51vvj',
            'USER': 'ioxmuxwysckuin',
            'PASSWORD': '78e36a7cba8d0ebf593b3487cfff0612271b321aff3091de292192acc5b23955',
            'HOST': 'ec2-23-23-128-222.compute-1.amazonaws.com',
            'PORT': 5432,
        }
    }