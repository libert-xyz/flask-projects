#default config
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\x94\x7f\xafN{\x8e7M\xeb\xc6\xe4\x90\xee2(\xc0\xc0\xbe\xd9\xac%Kz\x8fm'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] #DATABASE_URL='sqlite:///posts.db'
    print SQLALCHEMY_DATABASE_URI


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
