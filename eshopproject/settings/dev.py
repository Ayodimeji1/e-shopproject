from .base import *


DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:$$ayodimeji22@localhost:5432/eshop", conn_max_age=600
    )
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=q_%h3^%6^kgb*&bf+o3s5h9s@m%#+ie4%%@b%0$(+a5=k#!ht'

PAYSTACK_SECRET_KEY = 'sk_test_05e65d231a09f6b2d86495fa3e526d807287ccf8'
PAYSTACK_PUB_KEY = 'pk_test_abf9ebd652514f64bfb004be60e673c92224aa56'

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

# STRIPE_PUB_KEY = 'pk_test_51IuWjxSE3f2Hhlixj9Oallum2BlJd4uLegOYuWjZLSsT1lVSZoWb662n20CwxVVdtNo8aSaze9eFusyu04zUWOu500noO2YoEp'
# STRIPE_SECRET_KEY = 'sk_test_51IuWjxSE3f2HhlixGskjhHi3HxrY8HcuYSWoErToLgp1oX6A2hWC578F3sV0cyQ1smILbb8xHWkdOR6zCxyq8AJr00OXlbRi83'

STRIPE_PUB_KEY = "pk_test_TYooMQauvdEDq54NiTphI7jx"
STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

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