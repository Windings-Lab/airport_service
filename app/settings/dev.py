from .base import *

ALLOWED_HOSTS: list[str] = []

SECRET_KEY = "django-insecure-wi+16heuxz+hf72!s_h19o=#n=0mf3hzse*o98e6qoby7y41fr"

DEBUG = True

INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = ["127.0.0.1"]


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}