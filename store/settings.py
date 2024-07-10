import environ

from pathlib import Path

env = environ.Env(
    DEBUG=bool,
    SECRET_KEY=str,
    DOMAIN_NAME=str,

    REDIS_HOST=str,
    REDIS_PORT=str,

    DATABASE_NAME=str,
    DATABASE_USER=str,
    DATABASE_PASSWORD=str,
    DATABASE_HOST=str,
    DATABASE_PORT=str,

    EMAIL_HOST=str,
    EMAIL_PORT=int,
    EMAIL_HOST_USER=str,
    EMAIL_HOST_PASSWORD=str,
    EMAIL_USE_SSL=bool,
)

# ссылка до site_dj
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# '*' - сайт доступен на любом домене
ALLOWED_HOSTS = ['*']

DOMAIN_NAME = env('DOMAIN_NAME')

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
    'django_extensions',

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

# Redis
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')

# Caches
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
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
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_USE_SSL = env('EMAIL_USE_SSL')

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
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'
