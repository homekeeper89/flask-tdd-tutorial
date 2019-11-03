# application / views / error_handler
from . import *

@api_error.app_errorhandler(Exception)
def main_error_handler(error):
    if error.code != 500:
        try:
            desc = error.description['server']
        except Exception as e:
            desc = '예상치 못한 에러'
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'desc':desc
        }
    }
    current_app.logger.critical(response)
    return jsonify(response), error.code