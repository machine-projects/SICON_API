from src import db
import datetime


class UserProfileSytem(db.Model):
    __tablename__ = 'userProfileSytem'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    users = db.relationship("User",  backref=db.backref("users", lazy="dynamic"))

    profileSytem_id = db.Column(db.Integer, db.ForeignKey("profileSystem.id"), nullable=False)
    profileSystem = db.relationship("ProfileSystem",  backref=db.backref("profileSystem", lazy="dynamic"))

    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    def __init__(self, data):
        self.user_id = data.get('user_id')
        self.profileSytem_id = data.get('profileSytem_id')

    def __repr__(self):
        return f'<UserProfileSytem: {self.id}'
