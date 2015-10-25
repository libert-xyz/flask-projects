from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def show_url_for():
	return url_for("show_user_profile",username='Libert')


@app.route('/login', methods=['GET','POST'])
def login():
	if request.values:
		return 'user is %s' %request.values['user']
	else:
		return '<form method="post" action="/login"><input type="text" name="user"/><p><button type="submit">Submit</button>' 


@app.route('/user/<username>')
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




