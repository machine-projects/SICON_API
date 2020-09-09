from src import db
import datetime


class SystemPermission(db.Model):
    __tablename__ = 'systemPermission'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    system_id = db.Column(db.Integer, db.ForeignKey("system.id"), nullable=False)
    system = db.relationship("System",  backref=db.backref("system", lazy="dynamic"))

    name = db.Column(db.String(50), index=True, nullable=False)
    description = db.Column(db.String(200))
    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    def __init__(self, data):
        self.system_id = data.get('system_id')
        self.name = data.get('name')
        self.description = data.get('description')

    def __repr__(self):
        return f'<SystemPermission: {self.name}'
