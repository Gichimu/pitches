from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
   
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref = 'users', lazy="dynamic")
    comments = db.relationship('Comment', backref = 'users', lazy="dynamic")
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
    
    
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def create_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch_id):
        comments = Comment.query.filter_by(pitch_id = pitch_id).all()
        return comments

    def remove_comment(self):
        comment = Comment.query.filter_by(id = self.id).first()
        db.session.remove(comment)

    def __repr__(self):
        return f'Comment {self.body}'


class Pitch(db.Model):

    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer, primary_key=True)
    pitch_pic_loc = db.Column(db.String(255))
    pitch_body = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, user_id):
        pitches = Pitch.query.filter_by(user_id = user_id).all()
        return pitches

    def remove_pitch(self):
        pitch = Pitch.query.filter_by(id = self.id).first()
        db.session.delete(pitch)

    def __repr__(self):
        return f'Pitch {self.body}'
