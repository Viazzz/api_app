import os
from .base import *

DEBUG = False

ADMINS = [
    ('Alexandr M', 'mgma.developer@gmail.com'),
]

ALLOWED_HOSTS = ['*','www.perf-app-example.ru','perf-app-example.ru']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('POSTGRES_DB'),
       'USER': os.environ.get('POSTGRES_USER'),
       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
       'HOST': 'db',
       'PORT': 5432,
   }
}