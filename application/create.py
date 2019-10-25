# application/create.py
# 서버 객체를 생성, 환경 변수를 세팅 해준다.
from flask import Flask


def create_app(mode='dev'):
    app = Flask(__name__)
    if mode == 'dev':
        app.config['DEBUG'] = True
    
    from .src.views import api_user
    app.register_blueprint(api_user)
    return app