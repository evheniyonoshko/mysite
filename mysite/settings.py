
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!u2rwup*w*7!$)x1d@$f_e0_oak8-xs+6ots7dwvw=rup0jfjx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite-test-task.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'storages',
    'posts',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
try:
    from mysite.settings_local import DATABASES
except:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'dvrkv2ounqlo3',
            'USER': 'pkyldlauoglxuy',
            'PASSWORD': 'd6744527f8e6266d7bcc9db45727187116b0fd6c855bd9becb42ce5b3dd83fc8',
            'HOST': 'ec2-176-34-111-152.eu-west-1.compute.amazonaws.com',
            'PORT': '5432',
        }
    }


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
SITE_ID = 1

AUTH_USER_MODEL = 'posts.User'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

LOGIN_URL = '/accounts/login/'

DISABLE_COLLECTSTATIC=1

AUTH_PROFILE_MODULE = 'posts.Profile'

CRISPY_TEMPLATE_PACK = 'bootstrap'

DEFAULT_FROM_EMAIL = 'yevhen.didi@gmail.com'
SERVER_EMAIL = 'yevhen.didi@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yevhen.didi@gmail.com'
EMAIL_HOST_PASSWORD = 'literbolik'