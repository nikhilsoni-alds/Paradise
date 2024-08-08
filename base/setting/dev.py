from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9fym%!$t2qtslb!#9)m6g9lziwklhq+p@c)af5_5y@xdwsc$o4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'postgres',
        'HOST' : 'aws-0-ap-south-1.pooler.supabase.com',
        'PORT' : '6543',
        'USER' : 'postgres.novxeoncyiswwnrbskkv',
        'PASSWORD' : 'Paradisealds@88'
    }
}