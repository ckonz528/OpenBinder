from flask import *
from flask_sqlalchemy import SQLAlchemy
from time import time
from hashlib import md5
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'

db = SQLAlchemy(app)


def md5encode(text):
    return md5(bytes(text, encoding='utf-8')).digest().hex()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    privilege = db.Column(db.Integer, nullable=False)

    notes = db.relationship('Note', backref='uploader', lazy=True)

    def __repr__(self):
        return f'<User {self.privilege}@{self.id} ({self.username})>'


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False)
    filehash = db.Column(db.String(128), nullable=False, unique=True)
    tags = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Note File {self.filename} ({self.user_id})>'


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@app.route('/')
@app.route('/intro.html')
def home():
    return render_template('intro.html', page='intro')


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        flash('You are already logged in!')
        return redirect(url_for('list_notes'))
    if request.method == 'POST':
        success = checkLogin(
            request.form['username'], request.form['password'])
        if success is not None:
            user_id, admin = success
            session['logged_in'] = user_id
            session['admin'] = admin
            session['username'] = request.form['username']
            return redirect(url_for('list_notes'))
        flash('Login failed :(')
    return render_template('login.html', page='login')


@app.route('/logout')
def logout():
    if session.get('logged_in'):
        session.pop('logged_in')
        session.pop('admin')
        flash('Successfully logged out')
    else:
        flash('You are not logged in')
    return redirect(url_for('login'))


@app.route('/upload.html', methods=['GET', 'POST'])
def uploader():
    if not session.get('logged_in'):
        flash('You need to be logged in to upload notes!')
        return redirect(url_for('login'))
    if request.method == 'POST':
        if 'note' not in request.files or request.files['note'].filename == '':
            flash('ERROR! Please select a file!')
            return redirect(request.url)
        file = request.files['note']

        # get the filepath to save it to
        name, ext = os.path.splitext(file.filename)
        
        # verify that the file extension is valid
        if ext[1:].lower() not in ['pdf', 'doc', 'docx', 'txt', 'png', 'jpg', 'jpeg', 'gif', 'ppt', 'pptx', 'xlsx']:
            flash(f'File type {ext} not supported!')
            return redirect(request.url)
        
        unique_id = name + str(session['logged_in'])
        filehash = md5encode(unique_id) + ext
        path = os.path.join(app.config['UPLOAD_FOLDER'], filehash)

        # save the file
        file.save(path)

        # record it in the database
        note = Note(
            filename=file.filename,
            filehash=filehash,
            tags=request.form['tags'],
            user_id=session['logged_in'])
        db.session.add(note)
        db.session.commit()

        # serve the uploaded file
        return redirect(url_for('list_notes'))
    return render_template('upload.html', page='upload')


@app.route('/view/<filename>')
def view_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/delete/<filename>')
def delete_file(filename):
    note_to_delete = Note.query.filter_by(filehash=filename).first()
    if note_to_delete is None:
        flash('Could not find file to delete!')
        return redirect(url_for('list_notes'))

    db.session.delete(note_to_delete)
    db.session.commit()
    
    try:
        os.remove(os.path.join('uploads', filename))
    except:
        pass

    flash('Note deleted!')

    return redirect(url_for('list_notes'))


@app.route('/edit/<filename>')
def edit_file(filename):
    if not session.get('logged_in'):
        flash('You need to be logged in to view this!')
        return redirect(url_for('login'))

    note_to_edit = Note.query.filter_by(filehash=filename).first()
    if note_to_edit is None:
        flash('Could not find note to edit!')
        return redirect(url_for('list_notes'))
    
    if note_to_edit.user_id != session.get('logged_in'):
        flash('You do not have permission to edit this note!')
        return redirect(url_for('list_notes'))

    return render_template('edit.html', note=note_to_edit)
    
@app.route('/update', methods=['POST'])
def update_note():
    if not session.get('logged_in'):
        flash('You need to be logged in to edit notes!')
        return redirect(url_for('login'))

    note_id = request.form['id']
    note = Note.query.get(note_id)
    if note.user_id != session.get('logged_in'):
        flash('You do not have permission to edit this note!')
        return redirect(url_for('list_notes'))

    note.tags = request.form['tags']
    db.session.commit()
    
    flash('Note successfully edited!')
    return redirect(url_for('list_notes'))
    


@app.route('/list.html')
def list_notes():
    if session.get('logged_in'):
        current_user = User.query.get(session['logged_in'])
        return render_template('list.html', notes=current_user.notes, page='list')
    flash('You need to be logged in to view this!')
    return redirect(url_for('login'))


@app.route('/search.html')
def search_notes():
    if session.get('logged_in'):
        all_notes = Note.query.all()
        return render_template('search.html', notes=all_notes, page='search')
    flash('You need to be logged in to view this!')
    return redirect(url_for('login'))


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']

        if User.query.filter_by(username=username).first() is not None:
            flash('A user by that name already exists!')
        elif len(username) > 20:
            flash('Username too long!')
        elif len(username) < 5:
            flash('Username too short!')
        elif len(password) < 5:
            flash('Password too short!')
        elif password != confirm:
            flash('Passwords must match!')
        else:
            user = User(username=username, password=md5encode(password), privilege=0)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

def checkLogin(username, password):
    user = User.query.filter_by(username=username).first()
    if user is not None and user.password == md5encode(password):
        return user.id, user.privilege


app.secret_key = str(time())
if __name__ == "__main__":
    app.run(debug=True)
