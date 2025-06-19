#!/usr/bin/env python3
'''
Creates a Minimal Flask Application
'''

# Imports the Flask class. An instance of this class will be our
# WSGI application
from flask import Flask

from flask import request, render_template, jsonify

# To protect injection attacks
from markupsafe import escape

# Creates an instance of the Flask class (i.e. our WSGI application)
# The first argument is the application's module or package. We use
# '__name__' as a convenient shortcut.
# !!! NOTE: Make sure to not call your application flask.py because
# this would conflict with Flask itself.

app = Flask(__name__)

# We then use the route() decorator to tell Flask what URL should
# trigger our function
@app.route("/")
def hello_world():
    '''
    Returns the message we want to display in the user's browser.
    The default content type is HTML, so HTML in the string will
    be rendered by the browser.
    '''
    return jsonify({'message':'Hello, HNG!'})

@app.route('/user/<string:username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'<h1>User {escape(username)}</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Attempt Login'
    else:
        return 'Normal Behaviour'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
