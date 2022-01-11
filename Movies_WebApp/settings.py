import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = os.path.join(BASE_DIR, 'static_content')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Your SECRET_KEY'

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
    'django.contrib.postgres',

    # my apps
    'Main',
    'accounts',
    'Movie_app',
    'Person_app',
    'Vote_app',
    'User_IP',
    'Search',
    'Movie_Category',
    'Comment_app',
    'Series_app',
    'Favourite_App',
    'Stats_app',
    # third party app
    'django_render_partial',
    'bootstrap5',
    'simplejson',
    'sorl.thumbnail',
    'slugify',
    'embed_video',
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
    'User_IP.middleware.SaveIPAddressMiddleware',
    'accounts.middleware.RestrictNonAdminUsersMiddleware'
]

ROOT_URLCONF = 'Movies_WebApp.urls'

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
                'accounts.context_processors.add_my_login_form',
                'Main.context_processors.next_parameter',
            ],
        },
    },
]

WSGI_APPLICATION = 'Movies_WebApp.wsgi.application'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION':'default-locmemcache',
        'TIMEOUT':5,
    }
}
CSRF_USE_SESSIONS = True
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DB_NAME = "DB_NAME"
DB_USER = "DB_USER"
DB_PASSWORD = "DB_PASSWORD"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': '*',
        'PORT': '5432',
    }
}

if __name__ == '__main__':
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(CONTENT_DIR, 'tmp/emails')
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
DEFAULT_FROM_EMAIL = 'DEFAULT_FROM_EMAIL'
EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

ENABLE_USER_ACTIVATION = False
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = False
LOGIN_VIA_EMAIL_OR_USERNAME = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = True
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = False
SIGN_UP_FIELDS = ['username', 'email']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['email']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, 'assets')
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(CONTENT_DIR, 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media_root')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#######################

PAGINATE_BY = 12
