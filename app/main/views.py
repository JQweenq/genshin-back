from flask import render_template, Blueprint, request

main: Blueprint = Blueprint('main', __name__)

class Item:
    title: str
    url: str
    get_description: str
    get_attrs: str
    post_description: str
    post_attrs: str
    delete_description: str
    delete_attrs: str
    patch_description: str
    patch_attrs: str

    def __init__(self, **kwargs):
        for key in kwargs:
            self.__setattr__(key, kwargs[key])

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', items=[
        Item(
            title='Characters',
            url='./api/characters',
            get_description='Получить список персонажей',
            get_attrs='{\nid?: int\nfrom?: int\nto?: int\n}',
            post_description='Создать персонажа',
            post_attrs='{\nid?: int,\nname?: str,\nrarity?: int,\nname_en?: str,\nfull_name?: str,\ncard?: str,\nweapon?: str,\neye?: str,\nsex?: str\nbirthday?: int\nregion?: str\naffiliation?: str\nportrait?: str\ndescription?: str\n}',
            delete_description='Удалить персонажа',
            delete_attrs='{\nid: int\n}',
            patch_description='Изменить данные персонажа',
            patch_attrs='{\nid: int\nname?: str\nrarity?: int\nname_en?: str\nfull_name?: str\ncard?: str\nweapon?: str\neye?: str\nsex?: str\nbirthday?: int\nregion?: str\naffiliation?: str\nportrait?: str\ndescription?: str\n}'
        ),
        Item(
            title='Dictionary',
            url='./api/dictionary',
            get_description='Получить список слов',
            get_attrs='{\nid?: int\nfrom?: int\nto?: int\n}',
            post_description='Создать слово',
            post_attrs='{\nid: int\nword?: str\ntranslate?: str\nsubinf?: str\noriginal? str\n}',
            delete_description='Удалить слово',
            delete_attrs='{\nid: int\n}',
            patch_description='Изменить данные слова',
            patch_attrs='{\nid: int\nword?: str\ntranslate?: str\nsubinf?: str\noriginal? str\n}',
        ),
        Item(
            title='Wishes',
            url='./api/wishes',
            get_description='Получить список персонажей',
            get_attrs='{\nid?: int\nfrom?: int\nto?: int\n}',
            post_description='Создать персонажа',
            post_attrs='{\nid?: int\nname?: str\nversion?: str\nposter?: str\nrate_5?: int\nrate_4?: int\n}',
            delete_description='Удалить персонажа',
            delete_attrs='{\nid: int\n}',
            patch_description='Изменить данные персонажа',
            patch_attrs='{\nid: int\nname?: str\nversion?: str\nposter?: str\nrate_5?: int\nrate_4?: int\n}'
        )
    ])

@main.route('/login')
def login():
    return render_template('signin.html')

@main.route('/register')
def register():
    print(request.method)
    if request.method == 'POST':
        pass
    return render_template('signup.html')


