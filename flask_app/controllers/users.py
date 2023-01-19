from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# Page routes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration')
def register():
    return render_template('register.html')

@app.route('/user/<int:id>/past/comics')
def render_past_comics(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_data = {
            'id': session['user_id']
        }
        data = {
            'id': id
        }
        return render_template('past_reads.html', this_user=user.User.get_user_by_id(user_data), this_users_reads = user.User.get_user_with_comics(data))

# User Logic (login + registration)


@app.route('/register', methods=['post'])
def register_user():
    if not user.User.val_reg(request.form):
        return redirect('/registration')
    else:
        data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        session['user_id'] = user.User.create_user(data)
        return redirect('/dashboard')


@app.route('/login', methods=['post'])
def login_user():
    found_user = user.User.val_login(request.form)
    if not found_user:
        return redirect('/')
    else:
        session['user_id'] = found_user.id
        return redirect('/dashboard')


@app.route('/logout')
def clear_sesh():
    session.clear()
    return redirect('/')