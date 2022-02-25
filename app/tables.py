import json

from sqlalchemy.orm import QueryableAttribute

from app.extensions import db, bcrypt


class BaseModel:
    __abstract__ = True

    def to_dict(self, show=[], _hide=[], _path=[]):
        # hidden columns
        hidden = self._hidden_fields if hasattr(self, "_hidden_fields") else []
        default = self._default_fields if hasattr(self, "_default_fields") else []
        default.extend(['ID', 'EDIT_AT', 'CREATED_AT'])

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
        return {c.name: (getattr(self, c.name) if type(getattr(self, c.name)) == str or type(getattr(self, c.name)) == int else None if getattr(self, c.name) is None else int(getattr(self, c.name).timestamp())) for c in self.__table__.columns}

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


class Users(db.Model, BaseModel):
    __tablename__: str = 'USERS'

    ID: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TOKEN: db.Column = db.Column(db.String)
    USERNAME: db.Column = db.Column(db.String, nullable=False)
    PASSWORD: db.Column = db.Column(db.String, nullable=False)
    EMAIL: db.Column = db.Column(db.String, nullable=False) # unique=True
    IS_ADMIN: db.Column = db.Column(db.Boolean, nullable=False, default=False)
    EDITED_AT: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    CREATED_AT: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(),
                                      nullable=False)

    _hidden_fields = [
        'MODIFIED_AT',
        'CREATED_AT'
    ]

    def __init__(self, USERNAME, PASSWORD, EMAIL, IS_ADMIN):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.EMAIL = EMAIL
        self.IS_ADMIN = IS_ADMIN

    def __repr__(self) -> str:
        return '<User %r:%r>' % (self.uid, self.username)

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.hash, password)

    def hash_password(self, password: str) -> None:
        self.hash = bcrypt.generate_password_hash(password, 13).decode('ascii')


class Characters(db.Model, BaseModel):
    __tablename__ = 'CHARACTERS'

    ID: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NAME: db.Column = db.Column(db.String)
    RARITY: db.Column = db.Column(db.String)
    NAME_EN: db.Column = db.Column(db.String)
    FULL_NAME: db.Column = db.Column(db.String)
    CARD: db.Column = db.Column(db.BINARY)
    WEAPON: db.Column = db.Column(db.String)
    EYE: db.Column = db.Column(db.String(8))
    SEX: db.Column = db.Column(db.String(8))
    BIRTHDAY: db.Column = db.Column(db.String(10))
    REGION: db.Column = db.Column(db.String)
    AFFILIATION: db.Column = db.Column(db.String)
    PORTRAIT: db.Column = db.Column(db.BINARY)
    DEST: db.Column = db.Column(db.String)
    EDITED_AT: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    CREATED_AT: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    _hidden_fields = [
        'MODIFIED_AT',
        'CREATED_AT'
    ]

    _default_fields = [
        "NAME",
        "CREATED_AT",
    ]

    def __init__(self, NAME):
        self.NAME = NAME

    def __repr__(self):
        return f'{self.__dict__.keys()}'

class Dictionary(db.Model, BaseModel):
    __tablename__ = 'DICTIONARY'

    ID: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    WORD: db.Column = db.Column(db.String)
    TRANSLATE: db.Column = db.Column(db.String)
    SUBINF: db.Column = db.Column(db.String)
    ORIGINAL: db.Column = db.Column(db.String)
    EDITED_AT: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    CREATED_AT: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    _hidden_fields = [
        'MODIFIED_AT',
        'CREATED_AT'
    ]

    def __init__(self, WORD, TRANSLATE, SUBINF, ORIGINAL):
        self.WORD = WORD
        self.TRANSLATE = TRANSLATE
        self.SUBINF = SUBINF
        self.ORIGINAL = ORIGINAL

class Gebets(db.Model, BaseModel):
    __tablename__ = 'GEBETS'

    ID: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NAME: db.Column = db.Column(db.String)
    VERSION: db.Column = db.Column(db.String(8))
    POSTER: db.Column = db.Column(db.BINARY)
    RATE_5 = None
    RATE_4 = None
    EDITED_AT: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    CREATED_AT: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, NAME, VERSION):
        self.NAME = NAME
        self.VERSION = VERSION