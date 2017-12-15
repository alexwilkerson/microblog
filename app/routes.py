from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alex'}
    posts = [
            {
                'author': {'username': 'Alex'},
                'body': 'Beautiful day in New Orleans!'
            },
            {
                'author': {'username': 'Kimberly'},
                'body': 'The movie Mother! was so cool!'
            }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
