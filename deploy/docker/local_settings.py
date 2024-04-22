FRONTEND_HOST = 'https://worec.sagebrush.work'
PORTAL_NAME = 'Worship Recordings'
SECRET_KEY = ''
POSTGRES_HOST = 'db'
REDIS_LOCATION = "redis://redis:6379/1"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mediacms",
        "HOST": POSTGRES_HOST,
        "PORT": "5432",
        "USER": "mediacms",
        "PASSWORD": "",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# CELERY STUFF
BROKER_URL = REDIS_LOCATION
CELERY_RESULT_BACKEND = BROKER_URL

MP4HLS_COMMAND = "/home/mediacms.io/bento4/bin/mp4hls"

DEBUG = False
LOGIN_ALLOWED = True
REGISTER_ALLOWED = True
UPLOAD_MEDIA_ALLOWED = True
CAN_REPORT_MEDIA = False
MAX_MEDIA_PER_PLAYLIST = 500
UPLOAD_MAX_SIZE = 25000000000
USERS_CAN_SELF_REGISTER = True
USERS_NOTIFICATIONS = {
    'MEDIA_ADDED': False,
}
CAN_ADD_MEDIA = "advancedUser"

DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_USE_TLS = True
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
ADMIN_EMAIL_LIST = ['']