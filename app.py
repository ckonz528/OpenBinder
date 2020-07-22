from flask import *
from flask_sqlalchemy import SQLAlchemy
from time import time
from hashlib import md5
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    privelege = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'User {self.privelege}@{self.id} ({self.username})'

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


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
        flash('Login failed :(')
    return render_template('login.html')


@app.route('/secret.html')
def secret():
    if session.get('logged_in'):
        if session['admin']:
            return 'Top secret admin info!'
        return 'Secret non-admin info!'
    return redirect(url_for('login'))


@app.route('/upload.html', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        if 'note' not in request.files or request.files['note'].filename == '':
            flash('ERROR! Please select a file!')
            return redirect(request.url)
        file = request.files['note']
        name, ext = os.path.splitext(file.filename)
        filename = md5(bytes(name, encoding='utf-8')).digest().hex() + ext
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

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
