"""
Django settings for wresume project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$v32^f-3x4ft8zy2++6ss91&(x)fo#m**ld+9=tx!o43t09c7m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = config('ALLOWED_HOST', cast=Csv(), default='*')

# Application definition

SHARED_APPS = [
    'tenant_schemas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'widget_tweaks',
    'users',
    'blogs',
    'resumes',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
]

TENANT_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'resumes',
    'blogs'
]

INSTALLED_APPS = [
    'tenant_schemas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'widget_tweaks',
    'debug_toolbar',
    'users',
    'resumes',
    'blogs',
    'froala_editor',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    'localhost',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'wresume.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

WSGI_APPLICATION = 'wresume.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': config('DB_NAME', default='wresume'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': 5432
    }
}

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_files'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TENANT_MODEL = 'users.Client'

AUTH_USER_MODEL = 'users.User'

DEFAULT_FILE_STORAGE = 'wresume.utils.MyFileStorage'

TENANT_LIMIT_SET_CALLS = True

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'users.forms.SignUpForm',
    # 'add_email': 'allauth.account.forms.AddEmailForm',
    # 'change_password': 'allauth.account.forms.ChangePasswordForm',
    # 'set_password': 'allauth.account.forms.SetPasswordForm',
    # 'reset_password': 'allauth.account.forms.ResetPasswordForm',
    # 'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    # 'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}

ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'

ACCOUNT_USERNAME_MIN_LENGTH = 2

PUBLIC_SCHEMA_URLCONF = 'wresume.urls_public'

PUBLIC_SCHEMA_NAME = 'public'

LOGIN_URL = reverse_lazy('account_login')

SITE_DOMAIN = config('SITE_DOMAIN', default='localhost')
DEFAULT_USER_PASSWORD = config('DEFAULT_USER_PASSWORD', default='fjsnfjsnfj3m')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST', default='smtp.zoho.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='noreply@wresu.me')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='Greatness2011..')

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@wresu.me')

ADMIN_EMAILS = config('ADMIN_EMAILS', default=['neefemee@gmail.com', 'adeyemidamilola3@gmail.com'])

FROALA_EDITOR_PLUGINS = (
    'align', 'char_counter', 'code_beautifier', 'code_view', 'colors', 'draggable', 'emoticons',
    'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image',
    'inline_style',
    'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert',
    'quote', 'save', 'table',
    'url', 'video'
)

FROALA_STORAGE_BACKEND = 'wresume.utils.MyFileStorage'

CHROME_DRIVER_PATH = config('CHROME_DRIVER_PATH', default='chromedriver')
