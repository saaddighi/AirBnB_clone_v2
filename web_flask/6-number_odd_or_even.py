#!/usr/bin/python3
"""Start web application with multiple routings
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def diplay():
    """Return string when route queried
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def dplay(text):
    """Return string when route queried
    """
    return 'C ' + text.replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def dlay(text="is cool"):
    """Return string when route queried
    """
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def dpl(n):
    "return string if n is a number"
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def ply(n):
    "return html file if n is a number"
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numb(n):
    "return html file if n is a number"
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
