from app.main.docs import *
from flask import render_template, Blueprint, redirect, url_for

main = Blueprint('/', __name__)

routes = {
    'characters': characters,
    'dictionary': dictionary,
    'wishes': wishes,
    'weapons': weapons
}


@main.route('/')
@main.route('/<route>')
@main.route('/index')
@main.route('/index/<route>')
def index(route='characters'):
    return render_template('index.html', is_authenticated=False, routes=routes, methods=routes[route])


@main.route('/login')
def login():
    return render_template('auth.html')


# redirects
@main.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)
