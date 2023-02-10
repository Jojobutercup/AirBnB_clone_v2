#!/usr/bin/python3
#-*- coding: utf-8 -*
"""
Import the Flask class and Create an instance of the class
Author: Osariemen Uwuilekhue
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
