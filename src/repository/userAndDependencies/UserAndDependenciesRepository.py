from src import db
from src.model.users import User
from src.model.address import Address
from src.model.contact import Contact
from src.model.person import Person



class UserAndDependenciesRepository:

    def __init__(self):
        pass

    def get(self, playload):
        _id = playload.get('id')
        db.session.query(User)