# application/views/user.py
from . import *

@api_user.route('/')
def get_user():
    return 'HELLO USER'