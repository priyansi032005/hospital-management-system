from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

SITE_URL = "http://127.0.0.1:8000"
