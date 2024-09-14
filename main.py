from flask import Flask, render_template, request, redirect, url_for, session
from replit import db
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
my_secret = os.environ['REPLIT_DB_URL']

# Admin username
ADMIN_USERNAME = "your_admin_username_here"

# Helper function to get the last 5 messages
def get_last_five_messages():
    messages = []
    for key in sorted(db.keys(), reverse=True)[:5]:
        messages.append(db[key])
    return messages[::-1]

@app.route('/')
def home():
    user_id = request.headers.get('X-Replit-User-Id')
    user_name = request.headers.get('X-Replit-User-Name')
    if user_id:  # User is authenticated
        return render_template('home.html', logged_in=True, username=user_name)
    return render_template('home.html', logged_in=False)

@app.route('/chat')
def chat():
    user_id = request.headers.get('X-Replit-User-Id')
    user_name = request.headers.get('X-Replit-User-Name')

    if not user_id:  # User is not authenticated
        return redirect(url_for('home'))

    messages = get_last_five_messages()
    return render_template('chat.html', messages=messages, admin=user_name == ADMIN_USERNAME)

@app.route('/post_message', methods=['POST'])
def post_message():
    user_id = request.headers.get('X-Replit-User-Id')
    user_name = request.headers.get('X-Replit-User-Name')

    if not user_id:  # User is not authenticated
        return redirect(url_for('home'))

    message = request.form['message']
    timestamp = datetime.now().timestamp()
    db[str(timestamp)] = {
        'username': user_name,
        'message': message,
        'timestamp': timestamp
    }
    return redirect(url_for('chat'))

@app.route('/delete_message/<timestamp>')
def delete_message(timestamp):
    user_name = request.headers.get('X-Replit-User-Name')

    if user_name == ADMIN_USERNAME:
        db.pop(timestamp, None)
    return redirect(url_for('chat'))

@app.route('/logout')
def logout():
    # Clear any session data we might be storing
    session.clear()
    # Redirect to home page
    return redirect(url_for('home'))

@app.route('/login_redirect')
def login_redirect():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)