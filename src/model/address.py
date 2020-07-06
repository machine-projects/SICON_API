from src import db
# from src.model.person import Person
import datetime


class Address(db.Model):
    __tablename__ = 'address'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)
    person = db.relationship("Person",  backref=db.backref("person", lazy="dynamic"))
    neighborhood = db.Column(db.String(128), index=True)
    street = db.Column(db.String(128), index=True)
    number = db.Column(db.String(20), index=True)
    complement = db.Column(db.String(128), index=True)
    city = db.Column(db.String(128), index=True)
    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    # person_address = db.relationship("PersonAddress",  backref=db.backref("person_address", lazy="dynamic"))

    def __init__(self, data):
        self.person_id = data.get('person_id')
        self.neighborhood = data.get('neighborhood')
        self.street = data.get('street')
        self.number = data.get('number')
        self.complement = data.get('complement')
        self.city = data.get('city')

    def __repr__(self):
        if self.city and self.neighborhood and self.street and self.number:
            return f'<Address: {self.city}, {self.neighborhood}, {self.street}, {self.number}'
        return f'<Address: id:{self.id}'
