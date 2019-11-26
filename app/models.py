from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    '''
    Class that outlines the behaviour and attributes of the user
    '''
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    profile_pic_path = db.Column(db.String())
    comments = db.relationship('Comment', backref = 'user', lazy="dynamic")
    pitches = db.relationship('Pitch', backref = 'user', lazy="dynamic")
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'



class Comment(db.Model):
    '''
    Class that outlines the attributes of the comment class
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def __repr__(self):
        return f'Comment {self.body}'


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_pic_loc = db.Column(db.String(255))
    pitch_body = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='pitch', lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, user_id):
        pitches = Pitch.query.filter_by(user_id = cls.user_id).all()
        return pitches



    def remove_pitch(self):
        pitch = Pitch.query.filter_by(id = self.id).first()
        db.session.remove(pitch)

    def __repr__(self):
        return f'Pitch {self.body}'
