from .base import * 
from .base import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-gerlat+1adhko4fcn07pt+7ot-o!r(9amrvs)s2e3y@00#c298"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

