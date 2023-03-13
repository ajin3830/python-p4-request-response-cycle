#!/usr/bin/env python3

# after running  
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# cd into server then run python app.py

import os

from flask import Flask, request, current_app, g, make_response, redirect, abort, session

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())
    # os.getcwd(): current working directory of a process.

# @app.route('/')
# def index():
#     host = request.headers.get('Host')
#     appname = current_app.name
#     response_body = f'''<h1>The host for this page is {host}<h1>
#             <h2>The name of this application is {appname}</h2>
#             <h3>The path of this application on the user's device is {g.path}</h3>'''
            
#     status_code = 202
#     headers = {}
#     return make_response(response_body, status_code, headers)

# @app.route('/reginald-kenneth-dwight')
# def index():
#     return redirect('names.com/elton-john')

# session: a dictionary object that can be used to hold onto values 
# between multiple requests.
# this example don't work, theres no StageName class
# @app.route('/<stage_name>')
# def get_name(stage_name):
#     match = session.query('StageName').filter(StageName.name == stage_name)[0]
#     if not match:
#         abort(404)
#     return make_response(f'<h1>{stage_name} is an existing stage name!</h1>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
