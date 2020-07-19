from flask import *
from time import time

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('main.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('secret'))
    if request.method == 'POST':
        success, admin = checkLogin(
            request.form['username'], request.form['password'])
        if success:
            session['logged_in'] = True
            session['admin'] = admin
            return redirect(url_for('secret'))
        return render_template('login.html', msg='Login failed :(')
    return render_template('login.html')

@app.route('/secret.html')
def secret():
    if session.get('logged_in'):
        if session['admin']:
            return 'Top secret admin info!'
        return 'Secret non-admin info!'
    return redirect(url_for('login'))

def checkLogin(username, password):
    valid_credentials = [
        ('ckonz', 'tomato juice'),
        ('admin', 'hunter1')
    ]
    admins = ['admin']
    return (username, password) in valid_credentials, username in admins


app.secret_key = str(time())
if __name__ == "__main__":
    app.run(debug=True)

