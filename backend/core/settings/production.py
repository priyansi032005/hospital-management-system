from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '.onrender.com',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com'
]


SITE_URL = "https://hospital-management-system.onrender.com"
BASE_URL = SITE_URL