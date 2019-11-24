# application/src/views/__init__.py

from flask import Blueprint, abort, jsonify, current_app
from application.create import db

api_user = Blueprint('API FOR USER', __name__, url_prefix='/user')
api_error = Blueprint('API_ERROR_HANDLER', __name__)

from .user import *
from .error_handler import *