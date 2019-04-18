from http import HTTPStatus

from flask import Blueprint

from connections.models.person import Person
from connections.schemas import PersonSchema

blueprint = Blueprint('connections', __name__)


@blueprint.route('/people')
def get_people():
    people_schema = PersonSchema(many=True)
    people = Person.query.all()
    return people_schema.jsonify(people), HTTPStatus.OK
