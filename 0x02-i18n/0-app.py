#!/usr/bin/env python3
""" a simple flask application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """return the root page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host='0.0.0.0', debug=True)
