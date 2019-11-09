#  application/src/tests/
# 서버가 켜지는지 확인 하는 테스트 코드
from . import *

def test_server_run(flask_app):
    app = flask_app
    assert app is not None

@pytest.mark.parametrize('env, expected',
        [('dev', 'Development'),
        ('prod', 'Product'),
        ('test', 'Testing')
        ]
)
def test_server_env(env, expected):
    app = create_app(env)
    assert app.config['MESSAGE'] == expected

@pytest.mark.parametrize('env, expected',
        [('dev', 'Development'),
        ('prod', 'Product'),
        ('test', 'Testing')
        ]
)
def test_server_db(env, expected):
    app = create_app(env)
    assert app is not None
