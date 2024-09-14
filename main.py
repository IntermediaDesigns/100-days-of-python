from flask import Flask, render_template, redirect, request
from datetime import date

app = Flask(__name__)

def render_page(heading, content, theme=None, blog_links=None):
    today = date.today().strftime("%B %d, %Y")
    theme = request.args.get("theme", "light")
    if theme not in ["light", "dark"]:
        theme = "light"
    return render_template('template.html',
                           heading=heading,
                           date=today,
                           content=content,
                           theme=theme,
                           blog_links=blog_links)

@app.route('/', methods=["GET", "POST"])
def home():
    heading = "Welcome to my blog!"
    content = "This is the home page of my blog. Feel free to explore my posts!"
    blog_links = [
        {"title": "My First Blog Post", "url": "/blog1"},
        {"title": "Reflections on Flask", "url": "/blog2"}
    ]
    return render_page(heading, content, blog_links=blog_links)

@app.route('/blog1', methods=["GET", "POST"])
def blog1():
    try:
        heading = "My First Blog Post"
        content = "This is the content of my first blog post. It's exciting to start blogging!"
        blog_links = [{"title": "Return Home", "url": "/"}]
        return render_page(heading, content, blog_links=blog_links)
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/blog2', methods=["GET", "POST"])
def blog2():
    try:
        heading = "Reflections on Flask"
        content = "Flask is a great microframework for Python. It's simple to use and very flexible!"
        blog_links = [{"title": "Return Home", "url": "/"}]
        return render_page(heading, content, blog_links=blog_links)
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