from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./app/templates'))

characters_ico = env.get_template('icons/characters.svg').render()
dictionary_ico = env.get_template('icons/dictionary.svg').render()
wishes_ico = env.get_template('icons/wishes.svg').render()
weapons_ico = env.get_template('icons/weapons.svg').render()
get_ico = env.get_template('icons/get.svg').render()
post_ico = env.get_template('icons/post.svg').render()
delete_ico = env.get_template('icons/delete.svg').render()
patch_ico = env.get_template('icons/patch.svg').render()


@dataclass
class Route:
    icon: str
    title: str
    href: str
    methods: list


@dataclass
class Method:
    icon: str
    method: str
    description: str
    params: str
    results: str


gets = "Получение. В любом случае возвращяется список, даже при указании id. Указывается только id, либо же from и to. При указании всех полей, поля from и to не будут обрабатываться и вернется просто ответ на запрос с полем id."
posts = "Создание. Поле name является обязательным, остальные опциональные. Результатом выполнения является статус код и сообщение"
delete = "Удаление.  Поле id является обязательным, остальные опциональные. Результатом выполнения является статус код и сообщение"
patch = "Изменение. Все поля обязательные, attr - название изменяемого поля, value - значение поля, всегда строка."

characters = Route(
    icon=characters_ico,
    title='Characters',
    href='characters',
    methods=[
        Method(
            icon=get_ico,
            method='GET',
            description='Получить список персонажей.',
            params=
            '''id: int
            from: int
            to: int''',
            results=
            '''[{
                "rarity": 5,
                "id": 3,
                "created_at": 1655979604,
                "full_name": "Аякс",
                "weapon": "Лук",
                "sex": "Мужской",
                "region": "Снежная",
                "portrait": "https://media.discordapp.net/attachments/771051943559823413/986701407048572938/unknown.png?width=248&height=473",
                "name": "Тартилия",
                "modified_at": 1655979992,
                "name_en": "Tartalia",
                "card": "https://media.discordapp.net/attachments/771051943559823413/986701360999313418/unknown.png",
                "eye": "Гидро",
                "birthday": "20 июля",
                "affiliation": "Фатуи",
                "description": "Познакомьтесь с Тартальей, непредсказуемым воином из Снежной! Не питайте иллюзий, что вы понимаете его подлинные намерения. Не забывайте, что за этой невинной внешностью скрывается безжалостное орудие для убийства."
            }]'''
        ),
        Method(
            icon=post_ico,
            method='POST',
            description='Создать персонажа. name - обязательное поле.',
            params=
            '''name: str
            rarity: int
            name_en: str
            full_name: st
            card: str
            weapon: str
            eye: str
            sex: str
            birthday: int
            region: str
            affiliation: str
            portrait: str
            description: str''',
            results="OK"
        ),
        Method(
            icon=delete_ico,
            method='DELETE',
            description='Удалить персонажа.',
            params='id: int',
            results="Ok"
        ),
        Method(
            icon=patch_ico,
            method='PATCH',
            description='Изменить персонажа',
            params=
            '''id: int
            attr: str
            value: str''',
            results="Ok"
        )
    ],
)
dictionary = Route(
    icon=dictionary_ico,
    title='Dictionary',
    href='dictionary',
    methods=[
        Method(
            icon=get_ico,
            method='GET',
            description='Получить список слов.',
            params=
            '''id: int
            from: int
            to: int''',
            results=
            '''[{
            "id": 1,
            "translate": "[prep] до; прежде чем",
            "created_at": 1655980216,
            "original": null,
            "word": "aba",
            "modified_at": 1655980216,
            "subinf": "dead inside"
            }]'''
        ),
        Method(
            icon=post_ico,
            method='POST',
            description='Создать слово. word - обязательное поле.',
            params=
            '''
            word: str
            translate: str
            subinf: str
            original: str
            ''',
            results="Ok"
        ),
        Method(
            icon=delete_ico,
            method='DELETE',
            description='Удалить слово',
            params='id: int',
            results="Ok"
        ),
        Method(
            icon=patch_ico,
            method='PATCH',
            description='Изменить слово',
            params=
            '''id: int
            attr: str
            value: str''',
            results="Ok"
        )
    ],
)

wishes = Route(
    icon=wishes_ico,
    title='Wishes',
    href='wishes',
    methods=[
        Method(
            icon=get_ico,
            method='GET',
            description='Получить список молитв.',
            params=
            '''id: int
            from: int
            to: int''',
            results=
            '''[{
            "id": 1,
            title: "Пиршество они",
            version: "1.0",
            poster: "https://media.discordapp.net/attachments/771051943559823413/986701360999313418/unknown.png",
            rate_5: "Тарталия",
            rate_4: "Тарталия",
            "created_at": 1655980216,
            "modified_at": 1655980216,
            }]'''
        ),
        Method(
            icon=post_ico,
            method='POST',
            description='Создать молитву. title - обязательный параметр',
            params=
            '''
            title: str
            version: str
            poster: str
            rate_5: str
            rate_4: str''',
            results="ok"
        ),
        Method(
            icon=delete_ico,
            method='DELETE',
            description='Удалить молитву',
            params='id: int',
            results="Ok"
        ),
        Method(
            icon=patch_ico,
            method='PATCH',
            description='Изменить молитву',
            params=
            '''id: int
            attr: str
            value: str''',
            results="Ok"
        )
    ],
)

weapons = Route(
    icon=weapons_ico,
    title='Weapons',
    href='weapons',
    methods=[
        Method(
            icon=get_ico,
            method='GET',
            description='Получить список оружий.',
            params=
            '''id: int
            from: int
            to: int''',
            results=
            '''[{
            "id": 1,
            title: "Серебряный меч",
            icon: "",
            rarity: 5,
            damage: 64,
            dest: "Я хз что за поле",
            "created_at": 1655980216,
            "modified_at": 1655980216,
            }]'''
        ),
        Method(
            icon=post_ico,
            method='POST',
            description='Создать оружие. title - обязательный параметр',
            params=
            '''
            title: str
            icon: str
            rarity: int
            damage: int
            dest: str''',
            results="ok"
        ),
        Method(
            icon=delete_ico,
            method='DELETE',
            description='Удалить оружие',
            params='id: int',
            results="Ok"
        ),
        Method(
            icon=patch_ico,
            method='PATCH',
            description='Изменить оружие',
            params=
            '''id: int
            attr: str
            value: str''',
            results="Ok"
        )
    ],
)
