import os
import dj_database_url


SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {'default': dj_database_url.config()}

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

STATIC_URL = os.environ['STATIC_URL']
