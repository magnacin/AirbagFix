import os # Importante este parametro para poder utilizarlo en STATIC FILES
from pathlib import Path
# Los de abajo son import settings necesarios para desplegar la pagina en Heroku
import django_heroku # Se importa utileria para usar heroku y subir el sitio al servidor de Heroku
import dj_database_url
from decouple import config # instalar python-decouple en lugar de decouple. 


# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# DJANGO_AIRBAGFIX_SK
SECRET_KEY = os.getenv("SECRET_KEY", default = '') # Obtiene las variables de entorno que estan en otro lado. en este
# caso la pondre directamente fija aqui 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Para cuando trabajamos de manera local es True

ALLOWED_HOSTS = ['www.airbagfix.mx',
                 'airbagfix.mx','localhost', '127.0.0.1','airbagfix2025.onrender.com'] # Que sitios web se permite acceder

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic', # Permite que white noise ejecute en modo local los archivos
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'airbagfix_web', # Agrega la app nueva de airbag fix
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', #habilita whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware', # poner en este orden recomendado
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
        'DIRS': [BASE_DIR / 'templates']
        ,
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
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = config("DATABASE_URL", default="sqlite:///db.sqlite3")
DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL)
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Directorio donde Django guardará los archivos estáticos cuando se ejecute collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Directorios adicionales donde buscar archivos estáticos (como CSS e imágenes de tu app)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Asegúrate de que este directorio existe
]

# Configurar WhiteNoise para servir archivos estáticos en producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuracion de Django para enviar mail

EMAIL_HOST = 'smtpout.secureserver.net'  # Servidor SMTP
EMAIL_PORT = 587  # Puerto SMTP
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')  # Tomar de variables de entorno
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')  # Tomar de variables de entorno
EMAIL_USE_TLS = True

if os.getcwd() == '/app':
    DEBUG = False # Si estamos en vivo el directorio sera este y DEBUG es False