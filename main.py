from flask import Flask, render_template, redirect
from datetime import date

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to my blog!"


@app.route('/blog1')
def blog1():
    try:
        heading = "My First Blog Post"
        today = date.today().strftime("%B %d, %Y")
        content = "This is the content of my first blog post. It's exciting to start blogging!"
        return render_template('template.html',
                               heading=heading,
                               date=today,
                               content=content)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/blog2')
def blog2():
    try:
        heading = "Reflections on Flask"
        today = date.today().strftime("%B %d, %Y")
        content = "Flask is a great microframework for Python. It's simple to use and very flexible!"
        return render_template('template.html',
                               heading=heading,
                               date=today,
                               content=content)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/redirect_blog1')
def redirect_blog1():
    return redirect('/blog1')


@app.route('/redirect_blog2')
def redirect_blog2():
    return redirect('/blog2')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
