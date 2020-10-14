from src import db
import datetime


class System(db.Model):
    __tablename__ = 'system'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    description = db.Column(db.String(200))
    url = db.Column(db.String(200), index=True)
    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    systemPermission = db.relationship("SystemPermission", back_populates="system")
    profileSystem = db.relationship("ProfileSystem", back_populates="system")

    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.url = data.get('url')

    def __repr__(self):
        return f'<System: {self.name}'
