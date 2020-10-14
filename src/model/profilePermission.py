from src import db
import datetime


class ProfilePermission(db.Model):
    __tablename__ = 'profilePermission'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    profile_system_id = db.Column(db.Integer, db.ForeignKey("profileSystem.id"), nullable=False)
    system_permission_id = db.Column(db.Integer, db.ForeignKey("systemPermission.id"), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    systemPermission = db.relationship("SystemPermission", back_populates="profilePermission")
    profileSystem = db.relationship("ProfileSystem", back_populates="profilePermission")

    def __init__(self, data):
        self.system_permission_id = data.get('system_permission_id')
        self.profile_system_id = data.get('profile_system_id')

    def __repr__(self):
        return f'<ProfilePermission: {self.id}'
