from flask import Flask, request, redirect, render_template
from flask.wrappers import Request
from replit import db

app = Flask(__name__, static_url_path='/static')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        form = request.form
        name = form["name"]
        username = form["username"]
        password = form["password"]

        if username in db.keys():  
            return "Username already exists. Please choose a different username."
        else:  
            db[username] = {"name": name, "password": password}
            return redirect('/signup_success') 
    return render_template('signup.html')

@app.route('/signup_success')
def signup_success():
    return render_template('signup_success.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form
        
        username = form["username"]
        password = form["password"]

        if username in db:
            if db[username]["password"] == password:
                return redirect('/login_success')  
            else:
                return redirect("/nope")
        else:
            return redirect("/nope")

    return render_template('login.html')

@app.route('/login_success')
def login_sucess():
    return render_template('login_success.html')

@app.route("/nope")
def nope():
    return render_template('nope.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)