# application/src/tests
from . import *
def test_get_user(flask_client):
    api = "/user/"
    res = flask_client.get(api)
    assert res.status_code == 200

def test_post_user(flask_client):
    api = "/user/"
    data = {
        "NAME" :"matthew",
        "AGE" :"31",
        "HOBBY":"soccer",
        "JOBS" :"developer"
    }
    data = json.dumps(data)
    res = flask_client.post(api, data=data, headers={"Content-Type": "application/json"})
    assert res.status_code == 405
