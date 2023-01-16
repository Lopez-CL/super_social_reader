from flask_app import app
from flask_app.models import comic,user, comment
from flask import request, redirect, session, render_template

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