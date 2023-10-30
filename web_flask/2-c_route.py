#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
"""

=======
"""simple flask app
"""
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
from flask import Flask
app = Flask(__name__)


<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """c what
    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
