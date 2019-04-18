from factory import Faker, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from connections.database import db
from connections.models.person import Person


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:

        abstract = True
        sqlalchemy_session = db.session


class PersonFactory(BaseFactory):
    """Person factory."""

    email = Sequence(lambda n: f'person{n}@example.com')
    first_name = Faker('first_name')
    last_name = Faker('last_name')

    class Meta:

        model = Person
