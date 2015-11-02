from flask import Flask, url_for, request, render_template,redirect, flash, make_response, session
import logging
from logging.handlers import RotatingFileHandler
app = Flask(__name__)


@app.route('/login', methods=['GET','POST'])

def login():
	error = None
	if request.method == 'POST':

		if valid_login(
			request.form.get('username'),
			request.form.get('password')):

			#response = make_response(redirect(url_for('welcome')))
			#response.set_cookie('username', request.form.get('username'))
			session['username'] = request.form.get('username')

			return redirect(url_for('welcome'))

		else:
			error = "Incorrect Username and Password"
			app.logger.warning("Incorrect username or password for user (%s)",request.form.get("username"))
	return render_template('login.html',error=error)



def valid_login(username,password):
	if username==password:
		return True

	else:
		False

@app.route('/')

def welcome():
	#username = request.cookies.get('username')
	if 'username' in session:
		return render_template('welcome.html',username=session['username'])
	else:
		return redirect(url_for('login'))

@app.route('/logout')

def logout():
	#response = make_response(redirect(url_for('login')))
	#response.set_cookie('username','',expires=0)
	session.pop('username', None)


	return redirect(url_for('login'))


def show_user_profile(username):

	#return 'User: ' + str(username)
	return 'User: %s' %username


@app.route('/post/<int:id>')
def show_user_post(id):
	#return 'Post: ' + str(id)
	return 'Post: %d' %id


@app.route('/hello')
def hello():
	i = 2
	return "Hello Flask " + str(i)

##If app is running from the shell
if __name__ == '__main__':
	app.secret_key = "Paralelopipedo"

	#logging
	handler = RotatingFileHandler("error.log",maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	app.debug = True
	app.run()




