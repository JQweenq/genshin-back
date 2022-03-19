<<<<<<< HEAD
from flask import render_template, Blueprint, request, redirect
=======
from flask import render_template, Blueprint, request, redirect, url_for
>>>>>>> f63d0e31679f4c610799eb9c87a883a090d4b2bd

main: Blueprint = Blueprint('/', __name__)

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
            title = 'Characters',
            href = 'characters',
            methods = [
                Method(
                    route = 'api/characters',
                    method = 'GET',
                    description = 'Получить список персонажей',
                    params = '{\nid?: int\nfrom?: int\nto?: int\n}',
                ),
                Method(
                    route = 'api/characters',
                    method = 'POST',
                    description = 'Создать персонажа',
                    params='{\nid?: int,\nname?: str,\nrarity?: int,\nname_en?: str,\nfull_name?: str,\ncard?: str,\nweapon?: str,\neye?: str,\nsex?: str\nbirthday?: int\nregion?: str\naffiliation?: str\nportrait?: str\ndescription?: str\n}',
                ),
                Method(
                    route = 'api/characters',
                    method = 'DELETE',
                    description = 'Удалить персонажа',
                    params='{\nid: int\n}',
                ),
                Method(
                    route = 'api/characters',
                    method = 'PATCH',
                    description = 'Изменить персонажа',
                    params='{\nid: int\nname?: str\nrarity?: int\nname_en?: str\nfull_name?: str\ncard?: str\nweapon?: str\neye?: str\nsex?: str\nbirthday?: int\nregion?: str\naffiliation?: str\nportrait?: str\ndescription?: str\n}'
                )
            ],
        ),
    'dictionary':
        Route(
            title='Dictionary',
            href = 'dictionary',
            methods=[
                Method(
                    route='api/dictionary',
                    method='GET',
                    description = 'Получить список слов',
                    params='{\nid?: int\nfrom?: int\nto?: int\n}',
                ),
                Method(
                    route='api/dictionary',
                    method='POST',
                    description = 'Создать слово',
                    params='{\nid: int\nword?: str\ntranslate?: str\nsubinf?: str\noriginal? str\n}',
                ),
                Method(
                    route='api/dictionary',
                    method='DELETE',
                    description = 'Удалить слово',
                    params='{\nid: int\n}',
                ),
                Method(
                    route='api/dictionary',
                    method='PATCH',
                    description = 'Изменить слово',
                    params='{\nid: int\nword?: str\ntranslate?: str\nsubinf?: str\noriginal? str\n}',
                )
            ],
        ),
    'wishes':
        Route(
            title = 'Wishes',
            href = 'wishes',
            methods = [
                Method(
                    route = 'api/wishes',
                    method = 'GET',
                    description = 'Получить список молитв',
                    params='{\nid?: int\nfrom?: int\nto?: int\n}',
                ),
                Method(
                    route = 'api/wishes',
                    method = 'POST',
                    description = 'Создать молитву',
                    params='{\nid?: int\nname?: str\nversion?: str\nposter?: str\nrate_5?: int\nrate_4?: int\n}',
                ),
                Method(
                    route = 'api/wishes',
                    method = 'DELETE',
                    description = 'Удалить молитву',
                    params='{\nid: int\n}',
                ),
                Method(
                    route = 'api/wishes',
                    method = 'PATCH',
                    description = 'Изменить молитву',
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
        methods = routes[route]
    else:
        methods = None
    print(route)
    return render_template('index.html', routes=routes, methods=methods)


@main.route('/login')
def login():
    return render_template('auth.html', is_login=True)

@main.route('/register')
def register():
    return render_template('auth.html', is_login=False)


# redirects
@main.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)