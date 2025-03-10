import os
from pathlib import Path
import django_heroku
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", default='')  # Usa variables de entorno para mayor seguridad

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Cambia a False para producción

ALLOWED_HOSTS = [
    'www.airbagfix.mx',
    'airbagfix.mx',
    'localhost',
    '127.0.0.1',
    'airbagfix2025.onrender.com'
]

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # WhiteNoise para servir archivos estáticos
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'airbagfix_web',  # Tu aplicación
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise debe estar después de SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AribagFix_Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directorio de plantillas
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

WSGI_APPLICATION = 'AribagFix_Django.wsgi.application'

# Database
DATABASE_URL = config("DATABASE_URL", default="sqlite:///db.sqlite3")
DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL)
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directorio donde se recopilan los archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Directorio donde están tus archivos estáticos locales
]

# Configuración de WhiteNoise para servir archivos estáticos en producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de Django para enviar correos
EMAIL_HOST = 'smtpout.secureserver.net'  # Servidor SMTP
EMAIL_PORT = 587  # Puerto SMTP
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')  # Usa variables de entorno
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')  # Usa variables de entorno
EMAIL_USE_TLS = True

# Configuración para producción
if os.getcwd() == '/app':
    DEBUG = False  # Desactiva DEBUG en producción