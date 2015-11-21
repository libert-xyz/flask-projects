from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
#import sqlite3

#app objects
app = Flask(__name__)

#config.py
import os
app.config.from_object(os.environ['APP_SETTINGS'])
#create the sqlalchemy objects

db = SQLAlchemy(app)

from models import *


#app.database = 'sample.db'

#login required decorators

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))

    return wrap

@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    #g.db = connect_db()
    #cur = g.db.execute('select * from posts')
    #print cur
    #print cur.fetchall()
    #post_dic = {}
    #posts = []
    #for row in cur.fetchall():
    #    posts.append(dict(title = row[0], description = row[1]))

    #posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    #g.db.close()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():

    return "I'm Libert R Schmidt"

@app.route('/welcome')
def welcome():

    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
        else:
            error =  "Invalid Credentials. Please try again."

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():

    session.pop('logged_in', None)
    flash('You were logged out')

    return redirect(url_for('welcome'))

#def connect_db():
#    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True)
