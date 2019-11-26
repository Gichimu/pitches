from . import main
from flask import render_template, request, abort, redirect, url_for
from ..auth.forms import LoginForm
from flask_login import current_user
from ..models import User, Comment, Pitch
from .forms import pitchForm

@main.route('/')
def home():
    '''
    Route that defines the homepage
    '''
    logged_in = False
    if current_user.is_authenticated:
        logged_in = True

    return render_template('index.html', logged_in = logged_in)

@main.route('/profile/<uname>')
def profile(uname):

    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    pitches = Pitch.get_pitches(user.id)
    if pitches is not None:
        return render_template('profile/profile.html', pitches=pitches)
    else:
        return render_template('profile/profile.html')


@main.route('/profile/<uname>/create', methods=['GET','POST'])
def create_pitch(uname):

    # user = User.query.filter_by(username = uname).first()
    form = pitchForm()
    
    
    Pitch.pitch_body = form.body.data
    db.session.commit()

    return redirect(url_for('main.profile', uname=uname))

    



