#!/usr/bin/python3
"""Start web application with multiple routings
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def  display():
    """Return string when route queried
    """
    return 'Hello HBNB!'

@app.route("/hbnb")
def diplay():
    """Return string when route queried
    """
    return 'HBNB'

@app.route("/c/<text>")
def dplay(text):
    """Return string when route queried
    """
    return 'C ' + text.replace('_', ' ')

@app.route("/python/")
@app.route("/python/<text>")
def dlay(text= "is cool"):
    """Return string when route queried
    """
    return 'Python ' + text.replace('_', ' ')

if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
