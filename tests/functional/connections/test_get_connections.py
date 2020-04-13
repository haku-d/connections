from http import HTTPStatus

from tests.factories import ConnectionFactory

EXPECTED_FIELDS = [
    'id',
    'connection_type',
    'to_person',
    'from_person',
]


def test_get_connections(db, testapp):
    ConnectionFactory.create_batch(10)
    db.session.commit()

    res = testapp.get('/connections')

    assert res.status_code == HTTPStatus.OK

    assert len(res.json) == 10
    for connection in res.json:
        for field in EXPECTED_FIELDS:
            assert field in connection
