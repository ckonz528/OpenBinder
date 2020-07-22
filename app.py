from flask import *
from flask_sqlalchemy import SQLAlchemy
from time import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    privelege = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'User {self.privelege}@{self.id} ({self.username})'

@app.route('/')
@app.route('/intro.html')
def home():
    return render_template('intro.html')

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

