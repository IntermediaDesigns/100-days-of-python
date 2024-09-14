from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

valid_users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    is_valid = False

    if username is not None and password is not None:
        try:
            if valid_users[username] == password:
                is_valid = True
        except KeyError:
            pass

    if is_valid:
        return redirect(url_for("welcome", username=username))
    else:
        return redirect(url_for("naughty_step"))

@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)

@app.route("/naughty_step")
def naughty_step():
    return render_template("naughty_step.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)