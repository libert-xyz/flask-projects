from flask import Flask, url_for, render_template , request ,  session , redirect

app= Flask(__name__)

@app.route('/')
def welcome():

    if 'username' in session:


        return render_template('welcome.html',user=session['username'])

    else:

        return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])

def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form.get('user'),request.form.get('pass')):

            session['username'] = request.form.get('user')
            return redirect(url_for('welcome'))

        else:
            error = "Incorrect User and Password"



    return render_template('login.html',error=error)


def valid_login(username,password):
    if username == password:
        return True
    else:
        return False

@app.route('/logout')

def logout():

    session.pop('username',None)
    return redirect(url_for('login'))


if __name__ == "__main__":

    app.secret_key = "Paralelopipedo"
    app.debug = True
    app.run("0.0.0.0")
