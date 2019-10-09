"""
Django settings for yndc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
sys.path.insert(0, "%s%sapps" % (BASE_DIR, os.sep))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# OVERRIDE ON PRODUCTION
SECRET_KEY = '1iw!u=%%+eldqxz16a=xk6)r5kmr1ov27-4^sv#19j+x4@&!gd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'board.context_processors.mobile'
            ]
        },
    },
]

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'easy_thumbnails'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'board.middleware.mobile.MobileMiddleware'
)

ROOT_URLCONF = 'yndc.urls'

WSGI_APPLICATION = 'yndc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Detroit'

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

LOGIN_URL = '/login/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_S3_FILE_OVERWRITE = False

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''

THUMBNAIL_ALIASES = {
    'board.House.photo': {
        'small': {'size': (50, 50), 'crop': True},
        'medium': {'size': (250, 250), 'crop': True},
        'large': {'size': (450, 450), 'crop': True},
        'print': {'size': (400, 0), 'crop': True},
    },
    'board.House.additional_photo': {
        'small': {'size': (50, 50), 'crop': True},
        'medium': {'size': (250, 250), 'crop': True},
        'large': {'size': (450, 450), 'crop': True},
        'print': {'size': (400, 0), 'crop': True},
    },
}
