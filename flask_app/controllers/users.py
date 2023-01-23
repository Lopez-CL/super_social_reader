from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
import os
bcrypt = Bcrypt(app)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# upload_folder = "flask_app/static/assets/image_folder"
# if not os.path.exists(upload_folder):
#     os.mkdir(upload_folder)

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
        return render_template('past_reads.html', this_user=user.User.get_user_by_id(user_data), this_users_reads=user.User.get_user_with_comics(data))


@app.route('/upload/page')
def render_upload_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('file_upload.html')


# User Logic (login + registration)


@app.route('/register', methods=['post'])
def register_user():
    if not user.User.val_reg(request.form):
        return redirect('/registration')
    else:
        data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password']),
            'file_name': None
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

# user_image upload
@app.route('/upload/image', methods=['POST'])
def add_image():
    if 'file' not in request.files:
        flash('*No file part', 'image_error')
        return redirect('/upload/page')
    print(request.files['file'].filename)
    file = request.files['file']
    if file.filename == '':
        flash('*No image selected for uploading','image_error' )
        return redirect('/upload/page')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('upload_image filename: ' + filename)
    data = {
        'file_name': filename,
        'id': session['user_id']
    }
    user.User.update_user_photo(data)
    return redirect('/dashboard')