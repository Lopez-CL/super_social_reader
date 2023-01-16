from flask_app import app
from flask_app.models import comic,user, comment
from flask import request, redirect, session, render_template

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
        return render_template('dashboard.html', this_user = user.User.get_user_by_id(data))

@app.route('/add/comic')
def render_add_comic_page():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template('add_comic.html')

#CRUD Logic

@app.route('/create/comic', methods=['post'])
def add_comic():
    if not comic.Comic.val_comic(request.form):
        return redirect('/add/comic')
    else:
        data = {
            'user_id': session['user_id'],
            'title': request.form['title'],
            'author': request.form['author'],
            'artist': request.form['artist'],
            'colorist': request.form['colorist'],
            'letterer': request.form['letterer'],
            'status': request.form['status'],
            'rating': None,
            'thought': None
        }
        comic.Comic.save(data)
        return redirect('/dashboard')

