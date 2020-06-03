from src import db
# from .person import Person
# from .address import Address
import datetime


class PersonAddress(db.Model):
    __tablename__ = 'person_address'
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["person_id", ],#"address_id"],
            ["person.id",]#"address.id"],
        ),
        db.ForeignKeyConstraint(
            ["address_id", ],#"address_id"],
            ["address.id",]#"address.id"],
        ),
    )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    address_id = db.Column(db.Integer, primary_key=True)
    address = db.relationship("Address")

    person_id = db.Column(db.Integer, primary_key=True)
    person = db.relationship("Person")

    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    def __init__(self, address_id, person_id):
        self.address_id = address_id
        self.person_id = person_id

    def __repr__(self):
        return f'<PersonAddress: {id}'
