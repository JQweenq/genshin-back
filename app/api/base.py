from app.tables import Base
from app.utils import dict_as_data
from flask import Response

status404 = Response("Not found", status=404)
status400 = Response("Bad request", status=400)
status200 = Response("Ok", status=200)


class BaseResource:
    @staticmethod
    def get(obj: Base, id=None, _from=None, to=None):
        response = obj.filter_table(obj, id, _from, to)

        if isinstance(response, list) and len(response) != 0:
            return [item.as_dict() for item in response]
        else:
            return status404

    @staticmethod
    def post(obj: Base, data, args):
        entity = obj(dict_as_data(args, data()))

        try:
            obj.update(entity)
        except:
            return status400
        return status200

    @staticmethod
    def delete(obj: Base, id):
        character = obj.query.filter(obj.id == id).first()

        try:
            obj.delete(character)
        except:
            return status404
        return status200

    @staticmethod
    def patch(obj: Base, data, id, attr, value):
        try:
            character = obj.query.filter(obj.id == id).first()
            character.__setattr__(attr, value)
            character.update(character)
            return status200
        except AttributeError:
            return status404
