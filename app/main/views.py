import os
from app.main.docs import *
from flask import render_template, Blueprint, redirect, url_for, send_from_directory, current_app

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


@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
