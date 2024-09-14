from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Admin credentials
ADMIN_USERNAME = "lynjai"
ADMIN_PASSWORD = "password123"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Post {self.title}>'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    print("Home route called")
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('home.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Login route called")
    if request.method == 'POST':
        print("POST request received")
        username = request.form['username']
        password = request.form['password']
        print(f"Received username: {username}, password: {password}")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            print(f"Login successful. Session: {session}")
            return redirect(url_for('admin'))
        else:
            print("Invalid credentials")
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/admin')
def admin():
    print(f"Admin route called. Session: {session}")
    if not session.get('logged_in'):
        print("Not logged in, redirecting to login")
        return redirect(url_for('login'))
    print("Logged in, rendering admin template")
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('admin.html', posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
