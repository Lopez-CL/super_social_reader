from flask_app import app
from flask_app.models import comic, user, comment
from flask import request, redirect, session, render_template
from werkzeug.utils import secure_filename
import os
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# Page Renders

@app.route('/dashboard')
def render_dash():
    if 'user_id' not in session:
        return redirect('/')
    else:
        print(session['user_id'])
        data = {
            'id': session['user_id']
        }
        return render_template('dashboard.html', this_user=user.User.get_user_by_id(data), all_users_comics=comic.Comic.get_all_session_user_current_comics(data), all_comics=comic.Comic.get_all_comics_with_users())


@app.route('/add/comic')
def render_add_comic_page():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template('add_comic.html')


@app.route('/comic/<int:id>')
def render_comic_detail(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': id
        }
        user_data = {
            'id': session['user_id']
        }
        return render_template('current_read.html', this_user = user.User.get_user_by_id(user_data), this_comic = comic.Comic.grab_comic_by_id_with_user(data), all_comments = comment.Comment.get_comments_by_comic_id(data) )

@app.route('/update/comic/<int:id>')
def render_update_comic_page(id):
    if 'user_id' not in session:
        return redirect('/')
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': id
        }
        return render_template('update_comic.html', this_comic = comic.Comic.grab_comic_by_id(data))




# CUD Logic

@app.route('/create/comic', methods=['post'])
def add_comic():
    if 'user_id' not in session:
        return redirect('/')
    filename = None
    if not comic.Comic.val_comic(request.form):
        return redirect('/add/comic')
    else:
        if request.files['file'].filename != None or len(request.files['file'].filename) == 0:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER_COVER'], filename))
                print('upload_image filename: ' + filename)
        data = {
            'user_id': session['user_id'],
            'title': request.form['title'],
            'author': request.form['author'],
            'artist': request.form['artist'],
            'colorist': request.form['colorist'],
            'letterer': request.form['letterer'],
            'status': request.form['status'],
            'rating': None,
            'thought': None,
            'cover_art': filename
        }
        comic.Comic.save(data)
        return redirect('/dashboard')

@app.route("/update/<int:id>", methods=['post'])
def update_comic(id):
    if 'user_id' not in session:
        return redirect('/')
    if not comic.Comic.val_comic(request.form):
        return redirect(f'/update/comic/{id}')
    else:
        filename = request.form['file']
        print(request.form['file'])
        if request.files['file'].filename != None or len(request.files['file'].filename) != 0:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER_COVER'], filename))
                print('upload_image filename: ' + filename)
        data = {
            'user_id': session['user_id'],
            'title': request.form['title'],
            'author': request.form['author'],
            'artist': request.form['artist'],
            'colorist': request.form['colorist'],
            'letterer': request.form['letterer'],
            'status': request.form['status'],
            'rating':request.form['rating'],
            'thought': request.form['thought'],
            'cover_art': filename,
            'id': id
        }
        comic.Comic.update_comic(data)
        return redirect(f'/comic/{id}')

@app.route('/delete/comic/<int:id>')
def delete_comic(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': id
        }
        comic.Comic.delete(data)
        return redirect('/dashboard')