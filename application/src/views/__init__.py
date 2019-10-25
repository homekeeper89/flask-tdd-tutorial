# application/src/views/__init__.py
from flask import Blueprint

api_user = Blueprint('API FOR USER', __name__, url_prefix='/user')

from .user import *