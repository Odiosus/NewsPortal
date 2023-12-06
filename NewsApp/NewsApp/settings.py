# ✅импортируем самостоятельно, если еще не
import os
from pathlib import Path
from dotenv import load_dotenv


# загружаем ENV
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ✅добавили новое приложение
    'NewsPaper.apps.NewspaperConfig',
    # ⚠️подключаем еще приложения
    'django.contrib.sites',
    'django.contrib.flatpages',
    # ✅добавили фильтры
    'django_filters',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]

# ⚠️добавили самостоятельно
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # ⚠️добавили из модуля D1.3
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewsApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ✅добавили 'DIRS': [os.path.join(BASE_DIR, 'templates')]
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'NewsApp.wsgi.application'


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

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅Добавили самостоятельно для подгрузки стилей из папки static (модуль D1.5)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

# бэкенды аутентификации
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# дополнительные параметры — РЕГИСТРАЦИЯ И ВХОД ПО ПОЧТЕ
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию,
# необходимо добавить строчку
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}


# адрес сервера Яндекс-почты для всех один и тот же
EMAIL_HOST = 'smtp.yandex.ru'  
# порт smtp сервера тоже одинаковый
EMAIL_PORT = 465  
# ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, 
# иными словами, это всё то что идёт до собаки
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# пароль от почты
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') 
# Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, 
# но включать его здесь обязательно
EMAIL_USE_SSL = True  


ADMINS = [
    ('Maks', 'suchkow@ya.ru'),  # список всех админов в формате ('имя', 'их почта')
]

MANAGERS = [
    ('man1', 'man@nodog.com')
]

SERVER_EMAIL = os.getenv('SERVER_EMAIL')  # это будет у нас вместо аргумента FROM в массовой рассылке

#os.getenv('DEFAULT_FROM_EMAIL')
# здесь указываем уже свою ПОЛНУЮ почту, с которой будут отправляться письма
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SITE_URL = 'http://127.0.0.1:8000'

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается,
# можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
