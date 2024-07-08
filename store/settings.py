from pathlib import Path

# ссылка до site_dj
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+6l7_a0k4d+0f45q3ep(((!gj2x7uryjs*v1l5@$yzszr^+b@r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# '*' - сайт доступен на любом домене
ALLOWED_HOSTS = ['*']

DOMAIN_NAME = 'http://localhost:8000'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'debug_toolbar',

    'products',
    'orders',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]

# адрес к нашим урлам
ROOT_URLCONF = 'store.urls'

# шаблоны
TEMPLATES = [
    {
        # работа с шаблонами
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'products.context_processors.baskets',
            ],
        },
    },
]

WSGI_APPLICATION = 'store.wsgi.application'

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTION': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# БД:
# 1. для SQlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# 2. для PostgresSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'store_db',
        'USER': 'store_username',
        'PASSWORD': 'store_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

# Локализация проекта (смена языка)
USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# бд
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Users
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Отправка Emails
EMAIL_HOST = 'smtp.yandex.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'dj.s1te@yandex.ru'
EMAIL_HOST_PASSWORD = 'xknvrqczilbuxxtx'
EMAIL_USE_SSL = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# OAuth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
        ],
    }
}

# Celery settings v1
# CELERY_BACKEND_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'

# Celery settings v2
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'
