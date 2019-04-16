from http import HTTPStatus

from flask import Blueprint, request

blueprint = Blueprint('connections', __name__)


@blueprint.route('/')
def hello():
    return 'hello', HTTPStatus.OK
