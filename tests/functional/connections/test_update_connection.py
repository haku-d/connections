from http import HTTPStatus

import pytest
from tests.factories import ConnectionFactory


@pytest.fixture
def connection_payload():
    return {
        'connection_type': 'friend',
    }


def test_update_connection_success(db, testapp, connection_payload):
    connection = ConnectionFactory()
    db.session.commit()

    res = testapp.patch('/connections/{}'.format(connection.id), json=connection_payload)

    assert res.status_code == HTTPStatus.OK


def test_update_not_existing_connection(db, testapp, connection_payload):
    res = testapp.patch('/connections/0', json=connection_payload)

    assert res.status_code == HTTPStatus.NOT_FOUND
    assert res.json['description'] == 'Connection does not exist'


def test_update_connection_fail(db, testapp, connection_payload):
    connection = ConnectionFactory()
    db.session.commit()

    connection_payload['connection_type'] = 'mother-in-law'

    res = testapp.patch('/connections/{}'.format(connection.id), json=connection_payload)

    assert res.status_code == HTTPStatus.BAD_REQUEST
    assert res.json['description'] == 'Input failed validation.'
    errors = res.json['errors']
    assert 'Invalid enum member mother-in-law' in errors['connection_type']
