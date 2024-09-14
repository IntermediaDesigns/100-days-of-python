from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/linktree')
def linktree():
    return render_template('linktree.html')

@app.route('/novel')
def novel():
    return render_template('novel.html')

@app.route('/mokebeasts')
def mokebeasts():
    return render_template('mokebeasts.html')

@app.route('/battle')
def battle():
    return render_template('battle.html')

@app.route('/hangman')
def hangman():
    return render_template('hangman.html')

@app.route('/bingo')
def bingo():
    return render_template('bingo.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
