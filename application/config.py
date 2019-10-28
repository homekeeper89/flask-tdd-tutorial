# application/config.py
# 모든 config 설정들을 여기서 관리합니다.
# current_app.config 를 통해서도 접근이 가능합니다.

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    MESSAGE = 'Product'

class DevelopmentConfig(Config):
    DEBUG = True
    MESSAGE = 'Development'

class TestingConfig(Config):
    TESTING = True
    MESSAGE = 'Testing'

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)