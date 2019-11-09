# application/config.py
# 모든 config 설정들을 여기서 관리합니다.
# current_app.config 를 통해서도 접근이 가능합니다.

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://root@localhost/production'
    MESSAGE = 'Product'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'mysql://root@localhost/develop'
    MESSAGE = 'Development'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'mysql://root@localhost/staging'
    MESSAGE = 'Testing'

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)