
"""
Django settings for Kerimov project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# ========== БЕЗОПАСНОСТЬ ==========
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-local-classroom-demo-only-replace-in-production'
)

# ========== РЕЖИМ РАЗРАБОТКИ ==========
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'testserver',
]


# ========== ПРИЛОЖЕНИЯ ==========
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'KerimovAPK',
]


# ========== MIDDLEWARE ==========
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ========== URL И ШАБЛОНЫ ==========
ROOT_URLCONF = 'Kerimov.urls'

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

WSGI_APPLICATION = 'Kerimov.wsgi.application'


# ========== БАЗА ДАННЫХ POSTGRESQL ==========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'AirportF',
        'USER': 'postgres',
        'PASSWORD': '8998',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# ========== ВАЛИДАЦИЯ ПАРОЛЕЙ ==========
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


# ========== ЯЗЫК И ВРЕМЯ ==========
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# ========== СТАТИКА И МЕДИА ==========
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ========== ID ПО УМОЛЧАНИЮ ==========
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
