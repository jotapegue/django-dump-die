"""
Django settings for django_dump_die project.

Generated by 'django-admin startproject' using Django 3.0.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# region Secret Key Management

def create_key(path, length):
    """
    Creates project "secret key" in settings folder.
    """
    import string
    from django.utils.crypto import get_random_string

    # Generate key.
    key = get_random_string(
        length,
        string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    )

    # Write key to file.
    with open(path, 'w', encoding='utf-8') as _f:
        _f.write(key)

    return key


MIN_KEY_LENGTH = 50
KEY_PATH = os.path.join(BASE_DIR, 'SECRET_KEY')

# Attempt to open and validate secret key.
SECRET_KEY = ''
_io_error = False  # pylint: disable=invalid-name
try:
    with open(KEY_PATH, 'r', encoding='utf-8') as _f:
        SECRET_KEY = _f.read().strip()
except IOError:
    _io_error = True  # pylint: disable=invalid-name

if _io_error or len(SECRET_KEY) < MIN_KEY_LENGTH:
    SECRET_KEY = create_key(KEY_PATH, MIN_KEY_LENGTH)

# endregion Secret Key Management

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'dump_die.apps.DumpDieConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dump_die.middleware.DumpAndDieMiddleware',
]

ROOT_URLCONF = 'django_dump_die.urls'

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

WSGI_APPLICATION = 'django_dump_die.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# region Dump Die Settings

# List of Simple Types defined as strings that should not be recursively evaluated.
# EX: 'Cell' #  From openpyxl package
DJANGO_DD_ADDITIONAL_SIMPLE_TYPES = []

# Max recursion depth dd should process through.
# Setting to None will mean unlimited.
DJANGO_DD_MAX_RECURSION_DEPTH = 20

# Max number of iterables to show when outputing
# Setting to None will mean unlimited
DJANGO_DD_MAX_ITERABLE_LENGTH = 20

# Include private members that start with a single underscore
DJANGO_DD_INCLUDE_PRIVATE_MEMBERS = False

# Include magic methods that are enclosed with dunders
DJANGO_DD_INCLUDE_MAGIC_METHODS = False

# Include attributes / properties
DJANGO_DD_INCLUDE_ATTRIBUTES = True

# Include functions
DJANGO_DD_INCLUDE_FUNCTIONS = True

# Attribute types start expanded
DJANGO_DD_ATTRIBUTE_TYPES_START_EXPANDED = False

# Attributes start expanded
DJANGO_DD_ATTRIBUTES_START_EXPANDED = True

# Functions start expanded
DJANGO_DD_FUNCTIONS_START_EXPANDED = False

# Force light theme
DJANGO_DD_FORCE_LIGHT_THEME = False

# Force dark theme
DJANGO_DD_FORCE_DARK_THEME = False

# Define the color scheme to use
# {value} should be a string hexcode for color with hash symbol. EX: #FF88CC
# Format as follows:
# {
#     'light': {
#         'color': {value},
#         'background': {value},
#     },
#     'dark': {
#         'color': {value},
#         'background': {value}
#     },
#     'types': {
#         'arrow': {value},           #  Expand/Collapse arrow
#         'unique': {value},          #  Unique hash for class
#         'access_modifier': {value}, #  Access Modifier Char
#         'type': {value},            #  Complex Types (non-int, float, string, bool, None)
#         'attribute': {value},       #  Class attribute
#         'function': {value},        #  Class functions
#         'docs': {value},            #  Class function documentation
#         'constant': {value},        #  Class constants
#         'index': {value},           #  Index values for indexable types
#         'key': {value},             #  Key values for dict
#         'string': {value},          #  Strings
#         'bool': {value},            #  Bools
#         'number': {value},          #  Ints and Floats
#         'none': {value},            #  None
#         'empty': {value},           #  No Attributes or methods available
#     }
# }
DJANGO_DD_COLOR_SCHEME = None

# endregion Dump Die Settings
