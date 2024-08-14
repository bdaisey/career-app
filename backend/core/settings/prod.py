# core/settings/prod.py

from .base import *

import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# ALLOWED_HOSTS = ['your-production-domain.com']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }