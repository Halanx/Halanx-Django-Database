"""
Django settings for Halanx project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8@%*i+3ckqe4%al^pm!_56s&e&k%eym&tx3p0)r#b+39ww6zv!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['localhost', '127.0.0.1','52.38.36.228','ec2-52-38-36-228.us-west-2.compute.amazonaws.com']
ALLOWED_HOSTS = ['localhost', '127.0.0.1','34.208.181.152','ec2-34-208-181-152.us-west-2.compute.amazonaws.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'BatchBase',
    'Carts',
    'ItemsList',
    'OrderBase',
    'Products',
    'ShopperBase',
    'StoreBase',
    'UserBase',
    # Social login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    #  'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook'
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Halanx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Halanx.wsgi.application'


# Databases
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Mysql database in my pc
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'halan',
        'USER': 'halan',
        'PASSWORD': 'Pass-1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# RDS Database - enable on AWS
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Halanx',
        'USER': 'Halanx',
        'PASSWORD': 'Pass-1234',
        'HOST': 'halanx.c0vvfkdln5ew.us-west-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}
"""


# sqlite database
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# enable on aws
"""
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ubuntu/h/p/static'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ubuntu/h/p/media'

"""