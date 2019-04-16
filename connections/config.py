from os import environ


class Config(object):
    DB_HOST = environ.get('DB_HOST', 'mysql')
    DB_USER = environ.get('DB_USER', 'root')
    DB_PASSWORD = environ.get('DB_PASSWORD', 'very_secure_password')
    DB_NAME = environ.get('DB_NAME', 'connections_db')
    SQLALCHEMY_DATABASE_URI = (f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/'
                               f'{DB_NAME}?charset=utf8mb4')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_RECYCLE = 3600


class TestConfig(Config):
    TESTING = True
    DEBUG = True

    TEST_DB_HOST = environ.get('TEST_DB_HOST', 'mysql_test')
    TEST_DB_USER = environ.get('TEST_DB_USER', 'root')
    TEST_DB_PASSWORD = environ.get('TEST_DB_PASSWORD', 'very_secure_password')
    TEST_DB_NAME = environ.get('TEST_DB_NAME', 'connections_db_test')
    ENABLE_CACHE = False
    CELERY_TASK_ALWAYS_EAGER = True
    SQLALCHEMY_DATABASE_URI = (f'mysql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}/'
                               f'{TEST_DB_NAME}?charset=utf8mb4')
