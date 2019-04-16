from http import HTTPStatus

from tests.factories import PersonFactory

EXPECTED_FIELDS = [
    'id',
    'first_name',
    'last_name',
    'email',
]


def test_can_get_people(db, testapp):
    PersonFactory.create_batch(10)
    db.session.commit()

    res = testapp.get('/people')

    assert res.status_code == HTTPStatus.OK

    assert len(res.json) == 10
    for person in res.json:
        for field in EXPECTED_FIELDS:
            assert field in person
