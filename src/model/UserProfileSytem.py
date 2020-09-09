from src import db
import datetime


class UserProfileSytem(db.Model):
    __tablename__ = 'profileSytem'
  
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User",  backref=db.backref("user", lazy="dynamic"))

    profileSytem_id = db.Column(db.Integer, db.ForeignKey("profileSytem.id"), nullable=False)
    profileSytem = db.relationship("ProfileSytem",  backref=db.backref("profileSytem", lazy="dynamic"))

    creation_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())
    modification_date = db.Column(db.DateTime(), nullable=False,  default=datetime.datetime.utcnow())

    def __init__(self, data):
        self.system_id = data.get('system_id')
        self.name = data.get('name')

    def __repr__(self):
        return f'<UserProfileSytem: {self.id}'
