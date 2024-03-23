#!/usr/bin/python3
"""Start web application with multiple routings
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def  display():
    """Return string when route queried
    """
    return '“Hello HBNB!”'

@app.route('/hbnb')
def diplay():
    """Return string when route queried
    """
    return '“HBNB”'

@app.route('/c')
def dplay():
    """Return string when route queried
    """
    text = input()
    for i in text:
        '_' == ' '
    return f'C {text}'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
