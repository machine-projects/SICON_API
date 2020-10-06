from src import db
import datetime


class UserProfileSystem(db.Model):
    __tablename__ = 'userProfileSystem'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    profile_system_id = db.Column(db.Integer, db.ForeignKey("profileSystem.id"), nullable=False)
    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    
    users = db.relationship("User", back_populates="userProfileSystem")
    profileSystem = db.relationship("ProfileSystem", back_populates="userProfileSystem")

    def __init__(self, data):
        self.user_id = data.get('user_id')
        self.profile_system_id = data.get('profile_system_id')

    def __repr__(self):
        return f'<UserProfileSystem: {self.id}'
