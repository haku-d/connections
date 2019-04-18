from http import HTTPStatus

from connections.models.person import Person


def test_can_create_person(db, testapp):
    payload = {
        'first_name': 'Bob',
        'last_name': 'Loblaw',
        'email': 'bob.loblaw@lawblog.co',
    }

    res = testapp.post('/people', json=payload)

    assert res.status_code == HTTPStatus.CREATED

    for field in payload:
        assert res.json[field] == payload[field]
    assert 'id' in res.json

    person = Person.query.get(res.json['id'])

    assert person is not None
    for field in payload:
        assert getattr(person, field) == payload[field]
