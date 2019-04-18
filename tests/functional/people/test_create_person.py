from http import HTTPStatus

EXPECTED_FIELDS = [
    'id',
    'first_name',
    'last_name',
    'email',
]


def test_can_create_person(testapp):
    payload = {
        'first_name': 'Bob',
        'last_name': 'Loblaw',
        'email': 'bob.lowblaw@lawblog.co',
    }

    res = testapp.post('/people', json=payload)

    assert res.status_code == HTTPStatus.CREATED
