# core/settings/dev.py

from .base import *

import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', DEFAULT_SECRET_KEY)
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '::1',]

INSTALLED_APPS += [
    'debug_toolbar',
]

# Insert Debug Toolbar middleware after SecurityMiddleware
MIDDLEWARE.insert(
    MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1,
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)