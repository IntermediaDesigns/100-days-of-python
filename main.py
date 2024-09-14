from flask import Flask, render_template

app = Flask(__name__)

reflections = {
    77: {
        "repl_link":
        "https://replit.com/@imdesigns/Day77100Days",
        "reflection":
        "Today we learned how to use templating and redirecting to slim things down a bit."
    },
    78: {
        "repl_link":
        "https://replit.com/@imdesigns/Day78100Days",
        "reflection":
        "Today's challenge is to build a place to store your reflections on the next 22 days of code."
    },
}


@app.route('/')
def home():
    return "Welcome to the 100 Days of Code Reflections.\n\nTo access a day, type the day number after the forward slash, ex. /77 or /78."


@app.route('/<int:day_number>')
def day_reflection(day_number):
    print(f"Accessing day_reflection for day {day_number}")
    if day_number in reflections:
        return render_template(
            'reflection.html',
            day=day_number,
            repl_link=reflections[day_number]['repl_link'],
            reflection=reflections[day_number]['reflection'])
    else:
        return "Day not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
