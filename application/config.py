# application/config.py
# 모든 config 설정들을 여기서 관리합니다.
# current_app.config 를 통해서도 접근이 가능합니다.

class Config(object):
    DEBUG = False
    TESTING = False
    DB = {
        'id':'myid',
        'password':'super_secret',
        'host':'localhost',
    }
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{id}:{password}@{host}/production'\
            .format(id=Config.DB['id'], password=Config.DB['password'], host=Config.DB['host'])
    MESSAGE = 'Product'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{id}:{password}@{host}/develop'\
            .format(id=Config.DB['id'], password=Config.DB['password'], host=Config.DB['host'])
    MESSAGE = 'Development'

class StagingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{id}:{password}@{host}/staging'\
            .format(id=Config.DB['id'], password=Config.DB['password'], host=Config.DB['host'])
    MESSAGE = 'Testing'

config_by_name = dict(
    dev=DevelopmentConfig,
    staging=StagingConfig,
    prod=ProductionConfig
)