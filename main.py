from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/language')
@app.route('/language/<lang>')
def index(lang='english'):
    if lang.lower() == 'spanish':
        return render_template('spanish.html')
    else:
        return render_template('english.html')

@app.route('/language', methods=["GET"])
def language():
    lang = request.args.get('lang', 'english')
    if lang.lower() == 'spanish':
        return render_template('spanish.html')
    else:
        return render_template('english.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)