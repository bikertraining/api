import os
import sys
from email.utils import parseaddr

import environ

env = environ.Env(
    CSRF_TRUSTED_ORIGINS=(list, []),
    DATABASE_HOST=(str, ''),
    DATABASE_NAME=(str, ''),
    DATABASE_PASSWORD=(str, ''),
    DATABASE_PORT=(int, 5432),
    DATABASE_USER=(str, ''),
    EMAIL_ADMINS=(tuple, ()),
    EMAIL_DEFAULT_FROM=(str, ''),
    EMAIL_DEFAULT_SERVER_FROM=(str, ''),
    EMAIL_HOST=(str, ''),
    EMAIL_HOST_PASSWORD=(str, ''),
    EMAIL_HOST_PORT=(int, 25),
    EMAIL_HOST_SUBJECT_PREFIX=(str, ''),
    EMAIL_HOST_USE_SSL=(bool, False),
    EMAIL_HOST_USE_TLS=(bool, False),
    EMAIL_HOST_USER=(str, ''),
    EMAIL_MANAGERS=(tuple, ()),
    SECURITY_ALLOWED_HOSTS=(list, []),
    SECURITY_DEBUG=(bool, False),
    SECURITY_FERNET_KEY=(str, b''),
    SECURITY_SECRET_KEY=(str, '')
)

environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
Security
"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECURITY_SECRET_KEY')

# SECURITY WARNING: keep the secret key used in production secret!
# Used to encrypt/decrypt certain features in the database
FERNET_KEY = env.bytes('SECURITY_FERNET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('SECURITY_DEBUG')

# A list of strings representing the host/domain names that this Django site can serve.
ALLOWED_HOSTS = env('SECURITY_ALLOWED_HOSTS')

"""
Application
"""

# Django Applications
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'dj_rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
]

# Project Applications
INSTALLED_APPS.extend([
    'admin.coach',
    'admin.coupon',
    'admin.ecourse',
    'admin.price',
    'admin.schedule',
    'client.contact',
    'client.coupon',
    'client.ecourse',
    'client.payment',
    'client.price',
    'client.register',
    'client.schedule',
    'client.team',
    'database.default',
    'merchant',
    'utils'
])

"""
Middleware
"""

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

"""
URLs
"""

ROOT_URLCONF = 'application.urls'

"""
Template
"""

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
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]

"""
ASGI / WSGI Application
"""

WSGI_APPLICATION = 'application.wsgi.application'

"""
Database
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('DATABASE_HOST'),
        'NAME': env('DATABASE_NAME'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'PORT': env('DATABASE_PORT'),
        'USER': env('DATABASE_USER')
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
Password Validation
"""

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 5
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }
]

"""
Internationalization
"""

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

"""
Static files (CSS, JavaScript, Images)
"""

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

"""
Django Rest
"""

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

if DEBUG:
    # Enables DRF Forms
    REST_FRAMEWORK.get('DEFAULT_RENDERER_CLASSES').append('rest_framework.renderers.BrowsableAPIRenderer')
else:
    # Disables DRF Forms
    REST_FRAMEWORK.get('DEFAULT_RENDERER_CLASSES').append('utils.filters.BrowsableAPIRendererWithoutForms')

"""
Login Settings
"""

# Login / Redirect URL's
LOGIN_URL = '/api-auth/login/'
LOGIN_REDIRECT_URL = '/'

# Logout / Redirect URL's
LOGOUT_URL = '/api-auth/logout/'
LOGOUT_REDIRECT_URL = LOGIN_URL

"""
Email Settings
"""

# Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Hostname
EMAIL_HOST = env('EMAIL_HOST')

# Username
EMAIL_HOST_USER = env('EMAIL_HOST_USER')

# Password
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Port
EMAIL_PORT = env('EMAIL_HOST_PORT')

# Subject Prefix
EMAIL_SUBJECT_PREFIX = env('EMAIL_HOST_SUBJECT_PREFIX')

# SSL Support
EMAIL_USE_SSL = env('EMAIL_HOST_USE_SSL')

# TLS Support
EMAIL_USE_TLS = env('EMAIL_HOST_USE_TLS')

# From Email Address
DEFAULT_FROM_EMAIL = env('EMAIL_DEFAULT_FROM')

# From Server Email Address
SERVER_EMAIL = env('EMAIL_DEFAULT_SERVER_FROM')

# Set the administrator email address(es)
ADMINS = tuple(parseaddr(email) for email in env.list('EMAIL_ADMINS'))

# Set the manager email address(es)
MANAGERS = tuple(parseaddr(email) for email in env.list('EMAIL_MANAGERS'))

"""
COR Headers
"""

CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: *',
)
CORS_ORIGIN_ALLOW_ALL = True

"""
Debug Toolbar
"""

INTERNAL_IPS = ALLOWED_HOSTS

DEBUG_TOOLBAR_PANELS = [
    # 'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    # 'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    # 'debug_toolbar.panels.logging.LoggingPanel',
    # 'debug_toolbar.panels.redirects.RedirectsPanel',
    # 'debug_toolbar.panels.profiling.ProfilingPanel'
]

"""
CACHE
"""

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache'
    }
}

"""
CSRF
"""

CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS')

"""
SSL
"""

SECURE_HSTS_SECONDS = 0

"""
Session
"""

SESSION_COOKIE_AGE = 43200
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
