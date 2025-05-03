import os

from .base import *

# Deployment tips
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-wi+16heuxz+hf72!s_h19o=#n=0mf3hzse*o98e6qoby7y41fr",
)

DEBUG = False
