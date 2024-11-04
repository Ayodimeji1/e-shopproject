from .base import *


DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:$$ayodimeji22@localhost:5432/eshop", conn_max_age=600
    )
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY)'

PAYSTACK_SECRET_KEY = config('PAYSTACK_SECRET_KEY')
PAYSTACK_PUBLIC_KEY = config('PAYSTACK_PUBLIC_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# STATICFILES_DIRS = [
#      os.path.join(BASE_DIR, 'static'),
# ]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'portfolio_db',
#         'USER': 'postgres',
#         'PASSWORD': '$$ayo22django',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
