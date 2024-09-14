from flask import Flask, request, redirect, render_template, session
import sqlite3
import os, time
from replit import db

app = Flask(__name__)
app.secret_key = os.environ['SESSIONKEY']  # Set this in Replit's Secrets tab

# Database setup
def get_db():
    return db

def init_db():
    if 'users' not in db:
        db['users'] = {}

init_db()

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]

        if username in db['users']:
            return "Username already exists. Please choose a different username."
        else:
            db['users'][username] = {"name": name, "password": password}
            return redirect('/signup_success')
    return render_template('signup.html')

@app.route('/signup_success')
def signup_success():
    return render_template('signup_success.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in db['users'] and db['users'][username]["password"] == password:
            session['user'] = {'username': username, 'name': db['users'][username]["name"]}
            return redirect('/login_success')
        else:
            return redirect("/nope")

    return render_template('login.html')

@app.route('/login_success')
def login_success():
    return render_template('login_success.html')

@app.route("/nope")
def nope():
    return render_template('nope.html')

@app.route('/hello')
def hello():
    if 'user' in session:
        return render_template('hello.html', name=session['user']['name'])
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)