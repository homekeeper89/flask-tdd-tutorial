# application/src/tests/
# test시 공통으로 사용하는 것들(fixture)을 관리한다.

from . import *

@pytest.fixture()
def flask_app():
    app = create_app()

    app_context = app.app_context()
    app_context.push()

    yield app
    app_context.pop()

@pytest.fixture()
def flask_client(flask_app):
    return flask_app.test_client()