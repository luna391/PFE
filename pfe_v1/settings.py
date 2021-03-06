"""
Django settings for pfe_v1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o6q-97_j4dg1(c=!p7&cuecy!(x35&v@ztvlz!%ghh-3uubnh+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #added
    'django.contrib.sites',
    'userena',
    'south',
    'guardian',
    'easy_thumbnails',
    'accounts',
    'sms_verif',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ANONYMOUS_USER_ID = -1

SITE_ID = 1

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ROOT_URLCONF = 'pfe_v1.urls'

WSGI_APPLICATION = 'pfe_v1.wsgi.application'

# we only need the engine name, as heroku takes care of the rest

DATABASES = {'default': dj_database_url.config(default='postgres://postgres://ncrparrxvkpsxp:4zoHIiVUsDGegcs9mctoxZBXen@ec2-54-225-135-30.compute-1.amazonaws.com:5432/d2v8cqo927fhfj')}
#DATABASES = {
#    'default': {
#        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'proj_db',                      
#         'USER': 'proj_user',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT' : '5432',
     
#    }
#}

#DATABASES['default'] =  dj_database_url.config()

#DATABASES = {
#    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
#}

#DATABASES['default'] =  dj_database_url.config()

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {'default': dj_database_url.config(default='postgres://myuser@localhost:5432/mydb')}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'benabdallah.kmar@gmail.com'
EMAIL_HOST_PASSWORD = '%@luna21748232@%'



AUTH_PROFILE_MODULE = 'accounts.MyProfile'  
      
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'  
LOGIN_URL = '/accounts/signin/'  
LOGOUT_URL = '/accounts/signout/' 

