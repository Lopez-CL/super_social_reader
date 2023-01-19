from flask_app import app
from flask import redirect, request, session
from flask_app.models import user,comment,comic

@app.route('/comment/<int:id>', methods=['post'])
def submit_commit(id):
    if 'user_id' not in session:
        return redirect('/')
    if not comment.Comment.val_comment(request.form):
        return redirect(f'/comic/{id}') 
    data = {
        'user_id': session['user_id'],
        'comic_id': id,
        'content': request.form['content']
    }
    comment.Comment.save(data)
    return redirect(f'/comic/{id}')