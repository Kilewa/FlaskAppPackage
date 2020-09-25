from flask import render_template, redirect, url_for, abort, request
from . import main
#from flask_login import login_required, current_user
#from ..models import User, Comment, Pitch
#from .forms import UpdateProfile, CommentForm, PitchForm
#from .. import db, photos


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')