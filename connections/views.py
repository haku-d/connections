from http import HTTPStatus

from flask import Blueprint, jsonify

from connections.models.person import Person
from connections.schemas import PersonSchema

blueprint = Blueprint('connections', __name__)


@blueprint.route('/people', methods=['GET'])
def get_people():
    people_schema = PersonSchema(many=True)
    people = Person.query.all()
    return people_schema.jsonify(people), HTTPStatus.OK


@blueprint.route('/people', methods=['POST'])
def create_person():
    return (jsonify({'first_name': 'Bob', 'last_name': 'Loblaw', 'email': 'bob.loblaw@lawblog.co'}),
            HTTPStatus.CREATED)
