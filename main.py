from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('robot_check.html')

@app.route('/check', methods=['POST'])
def check():
    metal = request.form.get('metal')
    dream = request.form.get('dream')
    favorite_law = request.form.get('favorite_law').lower()

    is_robot = False

    if metal == 'yes':
        is_robot = True
    if dream == 'ed209':
        is_robot = True
    if 'kill' in favorite_law or 'exterminate' in favorite_law:
        is_robot = True

    if is_robot:
        return redirect(url_for('robot'))
    else:
        return redirect(url_for('human'))

@app.route('/robot')
def robot():
    return render_template('robot.html')

@app.route('/human')
def human():
    return render_template('human.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)