from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

if getenv("ENVIRONMENT") is None:
    # Если запускаемся локально
    import dotenv
    dotenv.load_dotenv(BASE_DIR.parent / ".env")

ENVIRONMENT = int(getenv("ENVIRONMENT"))

SECRET_KEY = getenv("DJANGO_SECRET_KEY")

DEBUG = True if ENVIRONMENT == 0 else False

ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", "localhost;127.0.0.1").split(";")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.sftapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    "default":
        {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": getenv("DJANGO_DB_NAME"),
            "USER": getenv("DJANGO_DB_USER"),
            "PASSWORD": getenv("DJANGO_DB_PASSWORD"),
            "HOST": getenv("DJANGO_DB_HOST"),
            "PORT": getenv("DJANGO_DB_PORT"),
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
