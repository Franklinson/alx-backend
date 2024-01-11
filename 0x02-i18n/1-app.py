#!/usr/bin/env python3
""" a simple flask application """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Configuring language and timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configuration
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


app = Flask(__name__)


@app.route('/')
def hello():
    """return the root page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host='0.0.0.0', debug=True)
