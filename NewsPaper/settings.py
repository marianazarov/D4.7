import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)$4@h8tlx&5^!2q(_fm3egt^x12&+fvy!*mq4=wf=i4k@#82j4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'simpleapp.apps.SimpleappConfig',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]


SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

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

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/news"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "marysanazarova"
EMAIL_HOST_PASSWORD = "lwdumenkslwewcyd"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "marysanazarova@yandex.ru"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}


CELERY_BROKER_URL = 'redis://default:53UUqozHD2iNDhnUfrgHaYj3uBIJxhel@redis-19544.c17.us-east-1-4.ec2.cloud.redislabs.com:19544'
CELERY_RESULT_BACKEND = 'redis://default:53UUqozHD2iNDhnUfrgHaYj3uBIJxhel@redis-19544.c17.us-east-1-4.ec2.cloud.redislabs.com:19544'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

SITE_URL = 'http://127.0.0.1:8000'


STATICFILES_DIRS = [
    BASE_DIR / "static"
]


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'error_and_critical': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true']
        },
        'warnings': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'warning',
            'filters': ['require_debug_true']
        },
        'error_and_critical': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'error_and_critical',
            'filters': ['require_debug_true']
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_and_critical',
            'filters': ['require_debug_false']
        },
        'generals': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general',
            'filters': ['require_debug_false']
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'general',
            'filters': ['require_debug_false']
        },
        'mail': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'error_and_critical',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'warnings', 'error_and_critical', 'generals'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['error_and_critical', 'mail'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['error_and_critical', 'mail'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['error_and_critical'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['error_and_critical'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}