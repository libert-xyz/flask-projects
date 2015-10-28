from flask import Flask, url_for, request, render_template,redirect
app = Flask(__name__)

@app.route('/')
def show_url_for():
	return url_for("show_user_profile",username='Libert')


@app.route('/login', methods=['GET','POST'])

def login():
	error = None
	if request.method == 'POST':

		if valid_login(
			request.form.get('username'),
			request.form.get('password')):
			return redirect(url_for('welcome',username=request.form.get('username')))

		else:
			error = "Incorrect Username and Password"
	
	return render_template('login.html',error=error)



def valid_login(username,password):
	if username==password:
		return True

	else:
		False

@app.route('/welcome/<username>')

def welcome(username):
	return render_template('welcome.html',username=username)

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
	app.debug = True
	app.run()




