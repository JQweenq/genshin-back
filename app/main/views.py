from flask import render_template, Blueprint, request

main: Blueprint = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('signin.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    print(request.method)
    if request.method == 'POST':
        pass
    return render_template('signup.html')
