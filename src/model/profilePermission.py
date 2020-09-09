from src import db
import datetime


class ProfilePermission(db.Model):
    __tablename__ = 'profilePermission'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    profile_system_id = db.Column(db.Integer, db.ForeignKey("profileSystem.id"), nullable=False)
    profile_system = db.relationship("ProfileSystem",  backref=db.backref("profileSystem", lazy="dynamic"))
    
    system_permission_id = db.Column(db.Integer, db.ForeignKey("systemPermission.id"), nullable=False)
    system_permission = db.relationship("SystemPermission",  backref=db.backref("systemPermission", lazy="dynamic"))

    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    def __init__(self, data):
        self.system_id = data.get('system_id')
        self.permission_id = data.get('permission_id')

    def __repr__(self):
        return f'<ProfilePermission: {self.id}'
