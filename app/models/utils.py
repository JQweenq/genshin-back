from datetime import datetime
from app.extensions import db


class CRUD:
    db = db

    ignore = [
        'created_at'
    ]

    def __init__(self, data):
        self.update_values(data)

    def update_values(self, data):
        for key in vars(data).keys():
            val = getattr(data, key)
            self.__setattr__(key, val)

    def as_dict(self, ignore=None) -> dict:
        ignore = ignore or self.ignore

        keys = vars(self).keys()
        _dict = dict.fromkeys(keys)

        for key in keys:
            if key not in ignore and not key.startswith('_'):
                attr = getattr(self, key)
                if isinstance(attr, (int, str, bool, list)):
                    _dict[key] = attr
                elif isinstance(attr, datetime):
                    _dict[key] = attr.timestamp()
            else:
                _dict.pop(key)  # delete key if ignoring

        return _dict

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
    def find_entity(base, id: int):
        return db.session.query(base).get(id)

    @staticmethod
    def find_entities(base, start: int, end: int):
        return db.session.query(base).filter(base.id.between(start, end)).all()

    @staticmethod
    def find_entities_starting_with(base, start: int):
        return db.session.query(base).filter(base.id >= start).all()

    @staticmethod
    def find_entities_ending_with(base, end: int):
        return db.session.query(base).filter(base.id <= end).all()

    @staticmethod
    def get_all_entities(base):
        return db.session.query(base).filter().all()
