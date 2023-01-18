#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """ displays text"""
    return 'C {:s}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ displays text"""
    return 'Python {:s}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def _number(n):
    """displays number"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number__template(n):
    """ displays num"""
    return render_template('5-number.html', n=n)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """diplays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display hbnb"""
    return 'HBNB'


if __name__ == "__main__":
    """ running app.route on 0.0.0.0:(port)5000"""
    app.run(host='0.0.0.0', port=5000)
