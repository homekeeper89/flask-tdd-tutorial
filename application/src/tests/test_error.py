# application/tests/test_error.py
# 모든 에러를 상황에서 맞춰서
from . import *


@pytest.mark.parametrize('error_code',[
    (400), (403)
])
def test_error_handler(flask_client, error_code):
    res = flask_client.get('/user/error/{}'.format(error_code))
    assert res.status_code == error_code