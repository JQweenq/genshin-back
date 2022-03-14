import json

from sqlalchemy.orm import QueryableAttribute
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db


class BaseModel:
    __abstract__ = True
    __tablename__: str

    id: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modified_at: db.Column = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    created_at: db.Column = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    _default_fields = [
        'id',
        'modified_at'
    ]

    _hidden_fields = [
        'created_at'
    ]

    def __init__(self, args: dict) -> None:
        self.update_values(args)

    def update_values(self, args: dict):
        for key in args.keys():
            if args[key] is not None:
                self.__setattr__(key, args[key])

    def to_dict(self, show=[], _hide=[], _path=[]):
        # hidden columns
        global prepend_path
        hidden = self._hidden_fields if hasattr(self, "_hidden_fields") else []
        default = self._default_fields if hasattr(self, "_default_fields") else []
        default.extend(['id', 'modified_at', 'created_at'])

        if not _path:
            _path = self.__tablename__.lower()

            def prepend_path(item):
                item.lower()

                if item.split(".", 1)[0] == _path:
                    return item
                if len(item) == 0:
                    return item
                if item[0] != ".":
                    item = ".%s" % item
                item = "%s%s" % (_path, item)
                return item

        _hide[:] = [prepend_path(x) for x in _hide]
        show[:] = [prepend_path(x) for x in show]

        columns = self.__table__.columns.keys()
        relationships = self.__mapper__.relationships.keys()
        properties = dir(self)

        data = dict()

        for key in relationships:
            if key.startswith("_"):
                continue
            check = "%s.%s" % (_path, key)
            if check in _hide or key in hidden:
                continue
            if check in show or key in default:
                _hide.append(check)
                is_list = self.__mapper__.relationships[key].uselist
                if is_list:
                    items = getattr(self, key)
                    if self.__mapper__.relationships[key].query_class is not None:
                        if hasattr(items, "all"):
                            items = items.all()
                    data[key] = []
                    for item in items:
                        data[key].append(
                            item.to_dict(
                                show=list(show),
                                _hide=list(_hide),
                                _path=("%s.%s" % (_path, key.lower())),
                            )
                        )
                else:
                    if (
                            self.__mapper__.relationships[key].query_class is not None
                            or self.__mapper__.relationships[key].instrument_class
                            is not None
                    ):
                        item = getattr(self, key)
                        if item is not None:
                            data[key] = item.to_dict(
                                show=list(show),
                                _hide=list(_hide),
                                _path=("%s.%s" % (_path, key.lower())),
                            )
                        else:
                            data[key] = None
                    else:
                        data[key] = getattr(self, key)

        for key in list(set(properties) - set(columns) - set(relationships)):
            if key.startswith("_"):
                continue
            if not hasattr(self.__class__, key):
                continue
            attr = getattr(self.__class__, key)
            if not (isinstance(attr, property) or isinstance(attr, QueryableAttribute)):
                continue
            check = "%s.%s" % (_path, key)
            if check in _hide or key in hidden:
                continue
            if check in show or key in default:
                val = getattr(self, key)
                if hasattr(val, "to_dict"):
                    data[key] = val.to_dict(
                        show=list(show),
                        _hide=list(_hide),
                        _path=('%s.%s' % (_path, key.lower())),
                    )
                else:
                    try:
                        data[key] = json.loads(json.dumps(val))
                    except:
                        pass

    def as_dict(self):
        return {c.name: (getattr(self, c.name) if type(getattr(self, c.name)) == str or type(
            getattr(self, c.name)) == int else None if getattr(self, c.name) is None else int(
            getattr(self, c.name).timestamp())) for c in self.__table__.columns}

    def filter_table(table, args=None, **kwargs, ) -> list:
        if args is not None:
            kwargs = args

        if kwargs['id'] is not None:
            return table.query.filter(table.id == kwargs['id']).first()
        else:
            if kwargs['from'] is not None and kwargs['to'] is not None:
                return table.query.filter(table.id > kwargs['from']).filter(table.id < kwargs['to']).all()
            else:
                if kwargs['from'] is not None:
                    return table.query.filter(table.id > kwargs['from']).all()
                elif kwargs['to'] is not None:
                    return table.query.filter(table.id < kwargs['to']).all()
                else:
                    return table.query.filter().all()

    @staticmethod
    def add(resource):
        db.session.add(resource)
        return db.session.commit()

    @staticmethod
    def delete(resource):
        db.session.delete(resource)
        return db.session.commit()

    @staticmethod
    def update(resource):
        db.session.add(resource)
        return db.session.commit()


class User(db.Model, BaseModel):
    __tablename__: str = 'USERS'

    username: str = db.Column(db.String, nullable=False)
    password: str = db.Column(db.String(128), nullable=False)
    email: str = db.Column(db.String, nullable=False, unique=True)
    is_admin: bool = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username: str, email: str, is_admin: bool = None) -> None:
        self.username = username
        self.email = email
        self.is_admin = is_admin

    def __repr__(self) -> str:
        return '<User %r:%r:%r:%r>' % (self.id, self.username, self.email, self.is_admin)

    @property
    def psw(self):
        raise AttributeError('`password` is not a readable attribute')

    @psw.setter
    def psw(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password) -> bool:
        return check_password_hash(self.password, password)


class Character(db.Model, BaseModel):
    __tablename__ = 'CHARACTERS'

    name: str = db.Column(db.String, unique=True)
    rarity: int = db.Column(db.Integer)
    name_en: str = db.Column(db.String, unique=True)
    full_name: str = db.Column(db.String, unique=True)
    card: str = db.Column(db.String)
    weapon: str = db.Column(db.String)
    eye: str = db.Column(db.String(8))
    sex: str = db.Column(db.String(8))
    birthday: str = db.Column(db.String(10))
    region: str = db.Column(db.String)
    affiliation: str = db.Column(db.String)
    protrait: str = db.Column(db.String)
    description: str = db.Column(db.String)

class Word(db.Model, BaseModel):
    __tablename__ = 'DICTIONARY'

    word: str = db.Column(db.String, unique=True)
    translate: str = db.Column(db.String)
    subinf: str = db.Column(db.String)
    original: str = db.Column(db.String)

    def __init__(self, word: str = None, translate: str = None, subinf: str = None, original: str = None) -> None:
        self.word = word
        self.translate = translate
        self.subinf = subinf
        self.original = original


class Wishe(db.Model, BaseModel):
    __tablename__ = 'WISHES'

    name: str = db.Column(db.String, unique=True)
    version: str = db.Column(db.String(8))
    poster: str = db.Column(db.String)
    rate_5 = db.Column(db.Integer, db.ForeignKey('CHARACTERS.id'))
    rate_4 = db.Column(db.Integer, db.ForeignKey('CHARACTERS.id'))

    def __init__(self, name: str = None, version: str = None, poster: str = None, rate_5: int = None,
                 rate_4: int = None):
        self.name = name
        self.version = version
        self.poster = poster
        self.rate_5 = rate_5
        self.rate_4 = rate_4


class Weapon(db.Model, BaseModel):
    __tablename__ = 'WEAPONS'

    name: str = db.Column(db.String, unique=True)
    icon: str = db.Column(db.String)
    rarity: int = db.Column(db.Integer)
    damage: int = db.Column(db.Integer)
    dest: str = db.Column(db.String)

    def __init__(self, name: str = None, icon: str = None, rarity: int = None, damage: int = None, dest: str = None):
        self.name = name
        self.icon = icon
        self.rarity = rarity
        self.damage = damage
        self.dest = dest