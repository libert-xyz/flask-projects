from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():

	return 'Hello Flask'


##If app is running from the shell
if __name__ == '__main__':
	app.run()




