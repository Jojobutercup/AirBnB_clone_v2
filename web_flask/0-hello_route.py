#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000

Created on Tue Sep  1 11:15:54 2020
@author: JOSEPHINE
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
