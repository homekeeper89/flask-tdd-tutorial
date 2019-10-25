#  application/src/tests/
# 서버가 켜지는지 확인 하는 테스트 코드

def test_server_run(flask_app):
    app = flask_app
    assert app is not None