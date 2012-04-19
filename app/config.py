# -*- config:utf-8 -*-
from datetime import timedelta
import os

project_name = "DUMMY_project.com"


class Config(object):
    DEBUG = False
    TESTING = False
    USE_X_SENDFILE = False

    # STATIC FILES
    BASE_PATH =   os.path.dirname(__file__)
    ROOT_PATH =   os.path.join(BASE_PATH, '../data/root/')
    STATIC_PATH = os.path.join(BASE_PATH, '../data/static/')
    STATIC_URL  = '/static/'
    MEDIA_PATH  = os.path.join(BASE_PATH, '../data/media/')
    MEDIA_URL   = '/media/'

    # DATABASE CONFIGURATION
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_dev.sqlite" % project_name
    SQLALCHEMY_ECHO = False

    CSRF_ENABLED = True
    SECRET_KEY = "VypXxN3ecFDPwu9yP3hLzqtTECGTw5ou"  # re.sub(os.linesep, '', os.urandom(24).encode('base64').rstrip())
    LOGGER_NAME = "%s_log" % project_name
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    # EMAIL CONFIGURATION
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    DEFAULT_MAIL_SENDER = "info@%s.com" % project_name


class Dev(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class Testing(Config):
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_test.sqlite" % project_name
    SQLALCHEMY_ECHO = False
