import os
import subprocess
import threading
import signal
import atexit
from pathlib import Path
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()  # Load .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
WEBPACK_PROCESS = None  # Store Webpack process globally

def run_webpack():
    """ Starts Webpack in a separate process """
    global WEBPACK_PROCESS
    if not WEBPACK_PROCESS:
        try:
            print("🚀 Starting Webpack...")
            WEBPACK_PROCESS = subprocess.Popen(
                ["npm", "run", "build"],  # Run Webpack in watch mode
                cwd=BASE_DIR,
                preexec_fn=os.setpgrp  # Allow independent termination
            )
        except FileNotFoundError:
            print("⚠️ Webpack not found! Run `npm install` to fix.")

def stop_webpack():
    """ Stops Webpack when Django stops """
    global WEBPACK_PROCESS
    if WEBPACK_PROCESS:
        try:
            print("🛑 Stopping Webpack...")
            os.killpg(os.getpgid(WEBPACK_PROCESS.pid), signal.SIGTERM)
        except ProcessLookupError:
            print("⚠️ Webpack process already stopped.")
        finally:
            WEBPACK_PROCESS = None  # Ensure process is cleared

if os.environ.get("RUN_MAIN") == "true":  # Prevent duplicate execution in Django autoreloader
    threading.Thread(target=run_webpack, daemon=True).start()

atexit.register(stop_webpack)  # Ensure Webpack stops when Django stops

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2jr*+=b&fr0j2!fnj6rnu4mu$g4*4xo*1(yube)_!k1n9p_c-8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

def global_settings(request):
    """ Make settings variables available in templates """
    return {
        "GOOGLE_CLIENT_ID": settings.SOCIALACCOUNT_PROVIDERS["google"]["APP"]["client_id"]
    }

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'QuantumTrade',

    'ai',
    'blockchain',
    'users',
    'marketplace',
    'django.contrib.sites',  # Required by allauth

    # Third-party authentication
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # Google OAuth Provider
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'QuantumTrade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'QuantumTrade/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'QuantumTrade.settings.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'QuantumTrade.wsgi.application'
SECURE_CROSS_ORIGIN_OPENER_POLICY = None

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

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default Django backend
    'allauth.account.auth_backends.AuthenticationBackend', # Social auth
)

# Google OAuth Credentials
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': GOOGLE_CLIENT_ID,
            'secret': GOOGLE_CLIENT_SECRET,
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }
}
# Specify the Site ID (usually, you can set it to 1 for development)
SITE_ID = 1

# Redirect URLs
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

# To allow email verification (optional but recommended)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_METHODS = {'email'}
