import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = 'cheesecake'
    # JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'cheese cake'
    # JWT_ALGORITHM = 'SH256'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    INTERNAL_URL = '127.0.0.1:5000'
    DEBUG = True
    # SERVER_NAME = 'localhost'
    FEATURE_FLAGS = {
        'firebase': False,
        'manage': True,
        'inventory': True,
        'finance': True,
        'reports': True
    }

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'username'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'password'  # os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:pass@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = "Dicks"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tests/test.db')
    APP_SLOW_DB_QUERY_TIME = 1


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class PythonAnywhereConfig(Config):
    INTERNAL_URL = 'www.example.com'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FEATURE_FLAGS = {
        'firebase': True,
        'manage': True,
        'inventory': False,
        'reports': True,
        'finance': False
    }
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'username'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'password'  # os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = ''


class DigitalOceanConfig(Config):
    INTERNAL_URL = ''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FEATURE_FLAGS = {
        'firebase': True,
        'manage': True,
        'inventory': False,
        'reports': True,
        'finance': False
    }
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'username'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'password'  # os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:pass@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Todo 31/8/2017 - herokuconfig



config = {
            'development': DevelopmentConfig,
            'testing': TestingConfig,
            'production': ProductionConfig,
            'default': DevelopmentConfig,
            "pythonanywhere": PythonAnywhereConfig,
            "digitalocean": DigitalOceanConfig
        }
