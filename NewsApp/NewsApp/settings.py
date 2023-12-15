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
    # ⚠️ добавили для кэширования
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
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

# TODO postgresql
# DATABASES = {
#     'default': {
#         # 'django.db.backends.sqlite3'
#         'ENGINE': 'django.db.backends.postgresql',
#         # BASE_DIR / 'db.sqlite3'
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '',  # TODO сделать через env
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

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

# формат даты, которую будет воспринимать наш задачник (модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается,
# можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# кэширование
CACHES = {
    'default': {
        # добавляем стандартное время ожидания в минуту (по умолчанию это 5 минут — 300 секунд)
        'TIMEOUT': 60,
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # указываем, куда будем сохранять кэшируемые файлы!
        # Не забываем создать папку cache_files внутри папки с manage.py!
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

# логирование
LOGGING = {
    # первый ключ version всегда определяется как 1
    'version': 1,
    # контролирует работу существующей (стандартной) схемы логирования
    'disable_existing_loggers': False,
    'style' : '{',
    # ключ — формат записи сообщений
    'formatters': {
        # (выводим в консоль) формат сообщения уровня DEBUG+ — время, уровень сообщения, сообщение
        'console_simple': {'format': '%(asctime)s %(levelname)s %(message)s'},
        # (выводим в консоль) формат сообщения уровня WARNING+ — время, уровень сообщения, сообщение, путь к источнику события
        'console_warning':{'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'},
        # (выводим в консоль) формат сообщения уровня ERROR и CRITICAL — время, уровень сообщения, сообщение, путь к источнику события, стэк ошибки
        'console_error':{'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'},
        # (выводим в файл general.log) формат сообщения уровня INFO+ — время, уровень сообщения, модуль, сообщение
        'general':{'format': '%(asctime)s %(levelname)s %(module)s %(message)s'},
        # (выводим в файл errors.log) формат сообщения уровня ERROR и CRITICAL — время, уровень сообщения, сообщение, путь к источнику события, стэк ошибки
        'error':{'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'},
        # (выводим в файл security.log) формат сообщения "уровня" SECURITY — время, уровень сообщения, модуль, сообщение
        'security': {'format': '%(asctime)s %(levelname)s %(module)s %(message)s'},
        # (отправляем на почту) формат сообщения уровня ERROR+ — время, уровень сообщения, сообщение, путь к источнику события
        'email': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
    },
    # ключ — фильтры
    'filters': {
        # в консоль сообщения отправляются только при DEBUG = True
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
        # на почту и в файл general.log — только при DEBUG = False
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
    },
    # ключ — обработчики
    'handlers': {
        # обработчик вывода сообщений уровня DEBUG+ в консоль
        'console_simple': {
            # уровень применения
            'level': 'DEBUG',
            # применяемый фильтр 
            'filters': ['require_debug_true'],
            # обработчик, отправляющий сообщения в консоль
            'class': 'logging.StreamHandler',
            # применяемый формат вывода
            'formatter': 'console_simple'},
        # обработчик вывода сообщений уровня WARNING+ в консоль    
        'console_warning': {
            # уровень применения
            'level': 'WARNING',
            # применяемый фильтр
            'filters': ['require_debug_true'],
            # обработчик, отправляющий сообщения в консоль
            'class': 'logging.StreamHandler',
            # применяемый формат вывода
            'formatter': 'console_warning'},
        # обработчик вывода сообщений уровня ERROR и CRITICAL в консоль    
        'console_error': {
            # уровень применения
            'level': 'ERROR',
            # применяемый фильтр
            'filters': ['require_debug_true'],
            # обработчик, отправляющий сообщения в консоль
            'class': 'logging.StreamHandler',
            # применяемый формат вывода
            'formatter': 'console_error'},
        # обработчик вывода сообщений уровня INFO+ в файл general.log
        'general':{
            # уровень применения
            'level' : 'INFO',
            # применяемый фильтр
            'filters': ['require_debug_false'],
            # обработчик, отправляющий сообщения в файл
            'class':'logging.FileHandler',
            # имя файла, в который отправляем сообщение
            'filename': 'general.log',
            # применяемый формат вывода
            'formatter': 'general'},
        # обработчик вывода сообщений уровня ERROR+ в файл errors.log
        'error': {
            # уровень применения
            'level': 'ERROR',
            # обработчик, отправляющий сообщения в файл
            'class': 'logging.FileHandler',
            # имя файла, в который отправляем сообщение
            'filename': 'errors.log',
            # применяемый формат вывода
            'formatter': 'error'},
        # обработчик вывода сообщений, связанных с безопасностью (security), в файл security.log
        'security':{
            # уровень применения
            'level': 'DEBUG',
            # обработчик, отправляющий сообщения в файл
            'class': 'logging.FileHandler',
            # имя файла, в который отправляем сообщение
            'filename': 'security.log',
            # применяемый формат вывода
            'formatter': 'security'},
        # обработчик вывода сообщений уровня ERROR+, отправляемых по почте
        'mail_admins': {
            # уровень применения
            'level': 'ERROR',
            # применяемый фильтр
            'filters': ['require_debug_false'],
            # обработчик, отправляющий сообщения по почте
            'class': 'django.utils.log.AdminEmailHandler',
            # применяемый формат вывода
            'formatter': 'email'
        },
    },
    # ключ — логгеры
    'loggers': {
        # регистратор
        'django': {
            # отправляет на консоль и в файл
            'handlers': ['console_simple', 'console_warning', 'console_error', 'general'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.request': {
            # отправляет в файл и на почту
            'handlers': ['error', 'mail_admins'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.server':{
            # отправляет в файл и на почту
            'handlers': ['error', 'mail_admins'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.template':{
            # отправляет в файл
            'handlers': ['error'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.db.backends':{
            # отправляет в файл
            'handlers': ['error'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.security':{
            # отправляет в файл
            'handlers': ['security'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        }
    }
}
