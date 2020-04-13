from http import HTTPStatus

from flask import abort, Blueprint
from marshmallow_enum import EnumField
from webargs.flaskparser import use_args

from connections.models.connection import Connection, ConnectionType
from connections.models.person import Person
from connections.schemas import ConnectionSchema, PersonSchema

blueprint = Blueprint('connections', __name__)


@blueprint.route('/people', methods=['GET'])
def get_people():
    people_schema = PersonSchema(many=True)
    people = Person.query.all()
    return people_schema.jsonify(people), HTTPStatus.OK


@blueprint.route('/people', methods=['POST'])
@use_args(PersonSchema(), locations=('json',))
def create_person(person):
    person.save()
    return PersonSchema().jsonify(person), HTTPStatus.CREATED


@blueprint.route('/connections', methods=['POST'])
@use_args(ConnectionSchema(), locations=('json',))
def create_connection(connection):
    connection.save()
    return ConnectionSchema().jsonify(connection), HTTPStatus.CREATED


@blueprint.route('/connections', methods=['GET'])
def get_connections():
    connections_schema = ConnectionSchema(many=True)
    connections = Connection.query.all()
    return connections_schema.jsonify(connections), HTTPStatus.OK


@blueprint.route('/connections/<int:connection_id>', methods=['PATCH'])
@use_args({'connection_type': EnumField(ConnectionType)}, locations=('json',))
def update_connection(args, connection_id):
    connection = Connection.query.get(connection_id)

    if not connection:
        abort(HTTPStatus.NOT_FOUND, 'Connection does not exist')

    connection.update(**args)

    return ConnectionSchema().jsonify(connection), HTTPStatus.OK
