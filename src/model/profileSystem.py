from src import db
import datetime


class ProfileSystem(db.Model):
    __tablename__ = 'profileSystem'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    system_id = db.Column(db.Integer, db.ForeignKey("system.id"), nullable=False)
    name = db.Column(db.String(50), index=True, nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    
    system = db.relationship("System", back_populates="profileSystem")
    userProfileSystem = db.relationship("UserProfileSystem", back_populates="profileSystem")
    profilePermission = db.relationship("ProfilePermission", back_populates="profileSystem")

    def __init__(self, data):
        self.system_id = data.get('system_id')
        self.name = data.get('name')

    def __repr__(self):
        return f'<ProfileSytem: {self.name}'
