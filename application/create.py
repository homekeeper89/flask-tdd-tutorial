# application/create.py
# 서버 객체를 생성, 환경 변수를 세팅 해준다.
from flask import Flask
import pymysql

def connect_db(config):
    conn = pymysql.connect(host=config['table'], 
            user=config['id'], passwd=config['pass'], db=config['database'], charset='utf8')
    return conn

def create_app(mode='dev'):
    app = Flask(__name__)
    
    from config import config_by_name
    app.config.from_object(config_by_name[mode])
    
    from logger import file_logger
    app.logger.addHandler(file_logger('CRITICAL'))
    config = {'database' : 'develop',
            'table':'USERS_TB',
            'id':'root',
            'pass':'wkdgns15-09',
            }
    conn = connect_db(config)
    import ipdb; ipdb.set_trace()

    from src.views import api_user
    from src.views import api_error
    app.register_blueprint(api_user)
    app.register_blueprint(api_error)
    
    return app