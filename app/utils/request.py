from typing import List

import flask
from flask import Request

from app.utils.datas import *


class RequestExt(Request):

    def parse(self, required: List[str] = None):
        if required is None:
            required = []

        match self.method:
            case 'GET':
                return self.choice_locales(GET, required)
            case 'POST':
                # todo parse POST
                return self.choice_locales(POST, required)
            case 'DELETE':
                return self.choice_locales(DELETE, required)
            case 'PATCH':
                return self.choice_locales(PATCH, required)
            case 'PUT':
                # todo parse PUT
                return None

    def choice_locales(self, data, required):
        data = data()
        if len(self.args):
            return self.parse_imd(data, self.args, required)
        elif len(self.form):
            return self.parse_imd(data, self.form, required)
        elif self.content_type is not None and self.content_type.lower() == 'application/json':
            return self.parse_json(data, self.json, required)
        else:
            return data

    def parse_imd(self, data, imdict, required):

        if self.check_required(required, imdict.keys()):
            return flask.abort(400, f'Required params: {required}')

        for key in list(set(vars(data)) & set(imdict.keys())):  # keys in data and mdict
            if len(values := imdict.getlist(key)) > 1:
                setattr(data, key, values)
                setattr(data, '_lists_is_empty', False)
                try:
                    data._lists.append(key)
                except AttributeError:
                    data._lists = [key]
            elif len(values) == 0:
                value = imdict.get(key)
                setattr(data, key, self.casting_to_type(value))
            else:
                value = imdict.get(key)
                setattr(data, key, self.casting_to_type(value))

        return data

    def parse_json(self, data, json: dict, required):
        if self.check_required(required, json.keys()):
            return flask.abort(400, f'Required params: {required}')

        for key in set(vars(data)) & set(json.keys()):
            setattr(data, key, json[key])

        return data

    def check_required(self, required: List[str], keys: List[str]):
        return not set(required).issubset(keys)

    def casting_to_type(self, value):
        if value == '':
            return None

        try:
            return int(value)
        except ValueError:
            pass

        try:
            return float(value)
        except ValueError:
            pass

        return value
