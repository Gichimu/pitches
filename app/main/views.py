from . import main
from flask import render_template
from ..auth.forms import LoginForm

@main.route('/')
def home():
    '''
    Route that defines the homepage
    '''

    return render_template('index.html')



