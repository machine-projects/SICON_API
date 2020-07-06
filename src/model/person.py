from src import db
# from src.model.users import User
# from src.model.personAddress import PersonAddress
import datetime


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type = db.Column(db.String(128), index=True, nullable=True)
    birth_date = db.Column(db.Date())
    name = db.Column(db.String(128), index=True)
    surname = db.Column(db.String(128), index=True)
    gender = db.Column(db.String(128))
    cpf = db.Column(db.String(128), index=True)
    company_name = db.Column(db.String(128), index=True)
    cnpj = db.Column(db.String(128), index=True)
    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow())

    # address = db.relationship("Address", backref=db.backref("address", lazy="dynamic"))
    # user = db.relationship("User", backref=db.backref("users", lazy="dynamic"))
    # person_address = db.relationship("PesonAddress", backref=db.backref("person_address", lazy="dynamic"))
    # contact = db.relationship("Contact", backref=db.backref("contact", lazy="dynamic"))

    def __init__(self, data_person):
        _type = data_person.get('type')
        birth_date = data_person.get('birth_date')
        name = data_person.get('name')
        surname = data_person.get('surname')
        gender = data_person.get('gender')
        cpf = data_person.get('cpf')
        company_name = data_person.get('company_name')
        cnpj = data_person.get('cnpj')
        
        self.type = _type
        self.birth_date = birth_date
        self.name = name
        self.surname = surname
        self.gender = gender
        self.cpf = cpf
        self.company_name = company_name
        self.cnpj = cnpj
    
    def __repr__(self):
        identification = ''
        if self.name or self.surname or self.company_name:
            identification = f'{self.name} {self.surname} {self.company_name}'
        return f'<Person: {identification}'