from dataclasses import dataclass
from flask import render_template, Blueprint, request, redirect, url_for, abort
from jinja2 import Environment, FileSystemLoader
from flask_login import login_required, current_user

main: Blueprint = Blueprint('/', __name__)
env = Environment(loader=FileSystemLoader('./app/templates/components'))


@dataclass
class Route:
    title: str
    href: str
    methods: list


@dataclass()
class Method:
    route: str
    method: str
    description: str
    params: str
    results: str


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
                    results=""
                ),
                Method(
                    route='api/characters',
                    method='POST',
                    description='Создать персонажа',
                    params='{\nid?: int,\nname?: str,\nrarity?: int,\nname_en?: str,\nfull_name?: str,\ncard?: str,\nweapon?: str,\neye?: str,\nsex?: str\nbirthday?: int\nregion?: str\naffiliation?: str\nportrait?: str\ndescription?: str\n}',
                    results=""
                ),
                Method(
                    route='api/characters',
                    method='DELETE',
                    description='Удалить персонажа',
                    params='{\nid: int\n}',
                    results=""
                ),
                Method(
                    route='api/characters',
                    method='PATCH',
                    description='Изменить персонажа',
                    params='{\nid: int\nname?: str\nrarity?: int\nname_en?: str\nfull_name?: str\ncard?: str\nweapon?: str\neye?: str\nsex?: str\nbirthday?: int\nregion?: str\naffiliation?: str\nportrait?: str\ndescription?: str\n}',
                    results=""
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
                    results=""
                ),
                Method(
                    route='api/dictionary',
                    method='POST',
                    description='Создать слово',
                    params='{\nid: int\nword?: str\ntranslate?: str\nsubinf?: str\noriginal? str\n}',
                    results=""
                ),
                Method(
                    route='api/dictionary',
                    method='DELETE',
                    description='Удалить слово',
                    params='{\nid: int\n}',
                    results=""
                ),
                Method(
                    route='api/dictionary',
                    method='PATCH',
                    description='Изменить слово',
                    params='{\nid: int\nword?: str\ntranslate?: str\nsubinf?: str\noriginal? str\n}',
                    results=""
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
                    results=""
                ),
                Method(
                    route='api/wishes',
                    method='POST',
                    description='Создать молитву',
                    params='{\nid?: int\nname?: str\nversion?: str\nposter?: str\nrate_5?: int\nrate_4?: int\n}',
                    results=""
                ),
                Method(
                    route='api/wishes',
                    method='DELETE',
                    description='Удалить молитву',
                    params='{\nid: int\n}',
                    results=""
                ),
                Method(
                    route='api/wishes',
                    method='PATCH',
                    description='Изменить молитву',
                    params='{\nid: int\nname?: str\nversion?: str\nposter?: str\nrate_5?: int\nrate_4?: int\n}',
                    results=""
                )
            ],
        )
}


@main.route('/')
@main.route('/<route>')
@main.route('/index')
@main.route('/index/<route>')
def index(route='characters'):
    return render_template('index.html', is_authenticated=current_user.is_authenticated, routes=routes, methods=routes[route])


@main.route('/login')
def login():
    return render_template('auth.html')


# redirects
@main.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)
