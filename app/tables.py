from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db, login
from app.data import UserData, CharacterData, WishData, WordData, WeaponData
from flask_login import UserMixin


class Base:
    __abstract__ = True
    __tablename__: str

    id: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modified_at: db.Column = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(),
                                       onupdate=db.func.current_timestamp())
    created_at: db.Column = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    _default_fields = [
        'id',
        'modified_at'
    ]

    _hidden_fields = [
        'created_at'
    ]

    def update_values(self, data: object):
        for key in data.__dict__.keys():
            self.__setattr__(key, getattr(data, key))

    def as_dict(self):
        keys = self.__dict__.keys()
        data = dict.fromkeys(keys)
        print(keys)

        for key in keys:
            if not key.startswith('_'):
                attr = getattr(self, key)
                if isinstance(attr, (int, str, bool, list)):
                    data[key] = attr
                elif isinstance(attr, datetime):
                    data[key] = attr.timestamp()
            else:
                data.pop(key)

        return data

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

    @staticmethod
    def find(base, id: str):
        return db.session.query(base).get(id)


@login.user_loader
def load_user(id):
    return db.session.query(User).get(id)


class User(db.Model, Base, UserMixin):
    __tablename__: str = 'users'

    username: str = db.Column(db.String, nullable=False, unique=True)
    hash: str = db.Column(db.String(128), nullable=False)
    email: str = db.Column(db.String, nullable=False, unique=True)
    is_admin: bool = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, data: UserData):
        self.update_values(data)

    @property
    def password(self):
        raise AttributeError('"password" is not a readable attribute')

    @password.setter
    def password(self, password):
        self.hash = generate_password_hash(password)

    def verify_password(self, password) -> bool:
        return check_password_hash(self.hash, password)


class Character(db.Model, Base):
    __tablename__ = 'characters'

    name: str = db.Column(db.String, unique=True)
    rarity: int = db.Column(db.Integer)
    name_en: str = db.Column(db.String)
    full_name: str = db.Column(db.String)
    card: str = db.Column(db.String)
    weapon: str = db.Column(db.String)
    eye: str = db.Column(db.String(8))
    sex: str = db.Column(db.String(8))
    birthday: str = db.Column(db.String(10))
    region: str = db.Column(db.String)
    affiliation: str = db.Column(db.String)
    portrait: str = db.Column(db.String)
    description: str = db.Column(db.String)

    def __init__(self, data: CharacterData):
        self.update_values(data)


class Word(db.Model, Base):
    __tablename__ = 'dictionary'

    word: str = db.Column(db.String, unique=True)
    translate: str = db.Column(db.String)
    subinf: str = db.Column(db.String)
    original: str = db.Column(db.String)

    def __init__(self, data: WordData) -> None:
        self.update_values(data)


class Wish(db.Model, Base):
    __tablename__ = 'wishes'

    title: str = db.Column(db.String, unique=True)
    version: str = db.Column(db.String(8))
    poster: str = db.Column(db.String)
    rate_5: str = db.Column(db.String)
    rate_4: str = db.Column(db.String)

    def __init__(self, data: WishData) -> None:
        self.update_values(data)


class Weapon(db.Model, Base):
    __tablename__ = 'weapons'

    title: str = db.Column(db.String, unique=True)
    icon: str = db.Column(db.String)
    rarity: int = db.Column(db.Integer)
    damage: int = db.Column(db.Integer)
    dest: str = db.Column(db.String)

    def __init__(self, data: WeaponData) -> None:
        self.update_values(data)
