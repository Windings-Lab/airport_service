from .base import *

import os

# Deployment tips
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-wi+16heuxz+hf72!s_h19o=#n=0mf3hzse*o98e6qoby7y41fr",
)

DEBUG = False


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASS"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": int(os.environ.get("DB_PORT", 5432)),
        "OPTIONS": {
            "sslmode": "require",
        },
        "DISABLE_SERVER_SIDE_CURSORS": True
    }
}