from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    '''
    Class that outlines the behaviour and attributes of the user
    '''
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy="dynamic")
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

    def __repr__(self):
        return f'User {self.body}'
