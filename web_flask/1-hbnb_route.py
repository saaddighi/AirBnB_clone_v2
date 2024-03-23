#!/usr/bin/python3
"""a script that starts a Flask web application
   web application is listening on 0.0.0.0, port 5000
   display “Hello HBNB!”
   display “HBNB”"""

from flask import  Flask

app = Flask(__name__)

@app.route('/', strict_slashes = False)
def display():
    """Return string when route queried
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes = False)
def diplay():
    """Return string when route queried
    """
    return 'HBNB'

if __name__ == "__main__":
    strict_slashes = False
    app.run(host='0.0.0.0', port= 5000)
