
#################
#### imports ####
#################
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

################
#### config ####
################
app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

app.register_blueprint(users_blueprint)


##########################
#### helper functions ####
##########################

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

################
#### routes ####
################


# use decorators to link the function to a url
@app.route('/')
@login_required
def home():

    posts = db.session.query(BlogPost).all()

    return render_template('index.html', posts=posts)  # render a template


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

####################
#### run server ####
####################

if __name__ == '__main__':
    app.run(debug=True)
