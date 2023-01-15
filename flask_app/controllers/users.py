from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
# Page routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def register():
    return render_template('register.html')

#User Logic (login + registration)

@app.route('/register', methods=['post'])
def register_user():
    if not
