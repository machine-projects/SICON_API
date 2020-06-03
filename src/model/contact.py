from src import db
import datetime


class Contact(db.Model):
    __tablename__ = 'contact'
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["person_id", ],
            ["person.id",]
        ),
    
    )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    person_id = db.Column(db.Integer, primary_key=True)
    person = db.relationship("Person")

    email = db.Column(db.String(65))
    cell_phone = db.Column(db.String(11))
    phone = db.Column(db.String(11))

    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    def __init__(self, person_id, email, cell_phone, phone):
        self.person_id = person_id
        self.email = email
        self.cell_phone = cell_phone
        self.phone = phone

    def __repr__(self):
        contact = 'id: {id}'
        if email: contact+= f', email:{email}' 
        if cell_phone: contact+= f', cellphone:{cell_phone}' 
        return f'<Contact: {contact}'
