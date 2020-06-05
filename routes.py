from flask import jsonify
from __main__ import app

@app.route('/')
@app.route('/check')
def get():
   return jsonify({ 'status' : 'ok' })


@app.route('/add_user')
def add_user():
   return jsonify({ 'status' : 'ok' })