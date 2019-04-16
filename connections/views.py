from http import HTTPStatus

from flask import Blueprint, jsonify

blueprint = Blueprint('connections', __name__)


@blueprint.route('/people')
def hello():
    return jsonify([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), HTTPStatus.OK
