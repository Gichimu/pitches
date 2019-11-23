from . import main
from flask import render_template

@main.route('/')
def home():
    '''
    Route that defines the homepage
    '''

    return render_template('index.html')