import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())
DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']


DATABASES = {
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
        'PORT': '5432',
        'DB_NAME': "",
}

db_connection1 = f'postgresql://{DATABASES['USER']}:{DATABASES['PASSWORD']}@{DATABASES['HOST']}:{DATABASES['PORT']}/{DATABASES['DB_NAME']}'


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///workouts.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///workouts.db"

    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""
    DEBUG = False

# DATABASES = {
#     'default': {
#         'NAME': DATABASE_NAME,
#         'USER': DATABASE_USER,
#         'PASSWORD': DATABASE_PASSWORD,
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
