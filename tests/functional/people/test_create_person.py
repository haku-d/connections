from http import HTTPStatus


def test_can_create_person(testapp):
    payload = {
        'first_name': 'Bob',
        'last_name': 'Loblaw',
        'email': 'bob.loblaw@lawblog.co',
    }

    res = testapp.post('/people', json=payload)

    assert res.status_code == HTTPStatus.CREATED

    for field in payload:
        assert res.json[field] == payload[field]
