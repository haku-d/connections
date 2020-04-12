from sqlalchemy.sql.expression import or_
from sqlalchemy.sql.functions import count

from connections.database import CreatedUpdatedMixin, CRUDMixin, db, Model
from connections.models.connection import Connection, ConnectionType


class Person(Model, CRUDMixin, CreatedUpdatedMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(145), unique=True, nullable=False)

    connections = db.relationship('Connection', foreign_keys='Connection.from_person_id')

    def mutual_friends(self, target):
        return (
            Person.query.join(Connection.to_person)
            .filter(
                or_(
                    Connection.from_person_id == self.id,
                    Connection.from_person_id == target.id,
                ),
                Connection.connection_type == ConnectionType.friend,
            )
            .group_by(Connection.to_person_id)
            .having(count(Connection.to_person_id) > 1)
            .all()
        )
