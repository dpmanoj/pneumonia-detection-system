"""
Django settings for root project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

import cloudinary

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lsw$m$75r-1jel=#cau+y022q2m1v@8om1#)15dy=90&j*6711'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ums',
    'crispy_forms',
    'ims',
    'diagnose',
    'cloudinary',
    'django_summernote',
    'blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'root.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dabhtk4kotv1ko',
        'USER': 'yfknghxmkvyfje',
        'PASSWORD': '85b1bf1ab169cf2b7206e66edc5d9f11e9720f92226fe563eb4f6e2513a8b080',
        'HOST': 'ec2-34-246-141-162.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
        'TEST': {
            'NAME': 'dabhtk4kotv1ko',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    # '/var/www/static/',
]
STATIC_ROOT = os.path.join(BASE_DIR, "static_files")

# Media root for uploading

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'anilfyp@gmail.com'
EMAIL_USER_TLS = True
EMAIL_HOST_PASSWORD = 'itisstrongpassword'

django_heroku.settings(locals())
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

cloudinary.config( 
  cloud_name = "anilpoudyal", 
  api_key = "189186639598883", 
  api_secret = "C0E4gkwAitl1xpKIaXPB5-8P39s" 
)
X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs4'