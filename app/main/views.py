from flask import render_template, Blueprint, request, redirect, url_for, abort
from jinja2 import Environment, FileSystemLoader
from flask_login import login_required, current_user

main: Blueprint = Blueprint('/', __name__)
env = Environment(loader=FileSystemLoader('./app/templates/components'))


class Route:
    title: str
    href: str
    methods: list

    def __init__(self, **kwargs):
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Method:
    route: str
    methods: list
    description: str
    params: str
    results: str

    def __init__(self, **kwargs):
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


routes = {
    'characters':
        Route(
            title='Characters',
            href='characters',
            methods=[
                Method(
                    route='api/characters',
                    method='GET',
                    description='Получить список персонажей',
                    params='{\nid?: int\nfrom?: int\nto?: int\n}',
                ),
                Method(
                    route='api/characters',
                    method='POST',
                    description='Создать персонажа',
                    params='{\nid?: int,\nname?: str,\nrarity?: int,\nname_en?: str,\nfull_name?: str,\ncard?: str,\nweapon?: str,\neye?: str,\nsex?: str\nbirthday?: int\nregion?: str\naffiliation?: str\nportrait?: str\ndescription?: str\n}',
                ),
                Method(
                    route='api/characters',
                    method='DELETE',
                    description='Удалить персонажа',
                    params='{\nid: int\n}',
                ),
                Method(
                    route='api/characters',
                    method='PATCH',
                    description='Изменить персонажа',
                    params='{\nid: int\nname?: str\nrarity?: int\nname_en?: str\nfull_name?: str\ncard?: str\nweapon?: str\neye?: str\nsex?: str\nbirthday?: int\nregion?: str\naffiliation?: str\nportrait?: str\ndescription?: str\n}'
                )
            ],
        ),
    'dictionary':
        Route(
            title='Dictionary',
            href='dictionary',
            methods=[
                Method(
                    route='api/dictionary',
                    method='GET',
                    description='Получить список слов',
                    params='{\nid?: int\nfrom?: int\nto?: int\n}',
                ),
                Method(
                    route='api/dictionary',
                    method='POST',
                    description='Создать слово',
                    params='{\nid: int\nword?: str\ntranslate?: str\nsubinf?: str\noriginal? str\n}',
                ),
                Method(
                    route='api/dictionary',
                    method='DELETE',
                    description='Удалить слово',
                    params='{\nid: int\n}',
                ),
                Method(
                    route='api/dictionary',
                    method='PATCH',
                    description='Изменить слово',
                    params='{\nid: int\nword?: str\ntranslate?: str\nsubinf?: str\noriginal? str\n}',
                )
            ],
        ),
    'wishes':
        Route(
            title='Wishes',
            href='wishes',
            methods=[
                Method(
                    route='api/wishes',
                    method='GET',
                    description='Получить список молитв',
                    params='{\nid?: int\nfrom?: int\nto?: int\n}',
                ),
                Method(
                    route='api/wishes',
                    method='POST',
                    description='Создать молитву',
                    params='{\nid?: int\nname?: str\nversion?: str\nposter?: str\nrate_5?: int\nrate_4?: int\n}',
                ),
                Method(
                    route='api/wishes',
                    method='DELETE',
                    description='Удалить молитву',
                    params='{\nid: int\n}',
                ),
                Method(
                    route='api/wishes',
                    method='PATCH',
                    description='Изменить молитву',
                    params='{\nid: int\nname?: str\nversion?: str\nposter?: str\nrate_5?: int\nrate_4?: int\n}'
                )
            ],
        )
}


@main.route('/')
@main.route('/index')
@main.route('/<route>')
@main.route('/index/<route>')
def index(route=None):
    if route is not None:
        try:
            methods = routes[route]
        except KeyError:
            return abort(404)
    else:
        methods = None
    if current_user.is_authenticated == True:
        sidebar = env.get_template('sidebar.html').render(routes=routes, is_authenticated=True,
                                                          current_user_name=current_user.username)
    else:
        sidebar = env.get_template('sidebar.html').render(routes=routes, is_authenticated=False)

    main = env.get_template('main.html').render(methods=methods)

    return render_template('index.html', sidebar=sidebar, main=main)


@main.route('/login')
def login():
    return render_template('auth.html', is_login=True)


@main.route('/register')
def register():
    return render_template('auth.html', is_login=False)


@main.route('/user/<user>')
@login_required
def profile(user):
    sidebar = env.get_template('sidebar.html').render(is_profile=True)

    main = env.get_template('main.html').render(is_profile=True)

    return render_template('index.html', sidebar=sidebar, main=main)


# redirects
@main.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)
