from datetime import datetime
from types import NoneType
from typing import Any

from app.extensions import db


def cast_to_json_type(var: Any) -> int | float | str | bool | list | None:
    if isinstance(var, (int, float, str, bool, list, NoneType)):
        return var
    elif isinstance(var, datetime):
        return var.timestamp()
    else:
        raise TypeError("Type is not defined")


class CRUD:
    db = db

    def __init__(self, data):
        self.update_values(data)

    def update_values(self, data):
        for key in vars(data).keys():
            val = getattr(data, key)
            self.__setattr__(key, val)

    def as_dict(self, ignore: list[str] | None = None, only: list[str] | None = None) -> dict:
        if ignore is None:
            ignore = []

        if only is None:
            only = []

        keys = vars(self).keys()
        _dict = dict.fromkeys(keys)

        for key in keys:
            if len(only) != 0:  # if only is not empty get keys else check ignore keys
                if key in only and not key.startswith('_'):
                    _dict[key] = cast_to_json_type(getattr(self, key))  # set value
                else:
                    _dict.pop(key)  # delete key if ignoring
            else:  # check ignore keys
                if key not in ignore and not key.startswith('_'):
                    _dict[key] = cast_to_json_type(getattr(self, key))  # set value
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
