from http import HTTPStatus


def test_can_get_people(testapp):
    res = testapp.get('/')
    assert res.status_code == HTTPStatus.OK
