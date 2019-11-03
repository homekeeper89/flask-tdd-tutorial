# application/views/user.py
from . import *

@api_user.route('/')
def get_user():
    return 'HELLO USER'

@api_user.route('/error/<int:error_code>')
def make_error_all(error_code):
    assert False, abort(error_code, {'server':'존재하지 않는 유저 정보'})