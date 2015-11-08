from flask_blog import app
from user.form import RegisterForm
from flask import render_template, redirect

@app.route('/login')
def login():
    return 'User Login'

@app.route('/register' , methods=('GET', 'POST'))

def register():

    form = RegisterForm()

    if form.validate_on_submit():
        return redirect('/success')
    return render_template('user/register.html', form=form)

@app.route('/success')

def success():
    return "Registered!"
