# application/src/tests
def test_get_user(flask_client):
    api = '/user/'
    res = flask_client.get(api)
    assert res.status_code == 200
