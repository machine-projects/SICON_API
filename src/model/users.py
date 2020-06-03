from src import db
from flask import current_app
from flask_bcrypt import Bcrypt
import datetime
# from .person import Person
# from src.model.person import Person

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["person_id"],
            ["person.id"],
        ),
    )

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    person_id = db.Column(db.Integer, primary_key=True, nullable=False)
    person = db.relationship("Person")
    username = db.Column(db.String(40), nullable=False,
                         unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    def __init__(self, username, password, is_admin):
        bcrypt = Bcrypt(current_app)
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.is_admin = is_admin

    def compare_password(self, password):
        bcrypt = Bcrypt(current_app)
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User: {self.username}'
