from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('main.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        msg = checkLogin(request.form['username'], request.form['password'])
        return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')

def checkLogin(username, password):
    if username == 'ckonz' and password == 'tomato juice':
        return 'Login successful!'
    return 'Login failed :('

app.run(debug=True)