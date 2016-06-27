#!usr/bin/python

from todoapp import app

@app.route('/')
def index():
    return '<h1> Hello world!<?h1>'

