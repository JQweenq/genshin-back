from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import IntegrityError

from app.models.utils import CRUD
from app.utils import dict_as_data
from flask import Response

status404 = Response("Not found", status=404)
status401 = Response("Not authorized", status=401)
status400 = Response("Bad request", status=400)
status200 = Response("Ok", status=200)

baseGetParser = RequestParser()

baseGetParser.add_argument('id', type=int)
baseGetParser.add_argument('start', type=int)
baseGetParser.add_argument('end', type=int)

baseDeleteParser = RequestParser()

baseDeleteParser.add_argument('id', type=int, required=True)

basePatchParser = RequestParser()

basePatchParser.add_argument('id', type=int, required=True)
basePatchParser.add_argument('attr', type=str, required=True)
basePatchParser.add_argument('value', type=str, required=True)


class BaseResource:
    @staticmethod
    def get(obj: CRUD, id: int = None, start: int = None, end: int = None):
        if id:
            response = obj.find_entity(obj, id)
        elif start and end:
            response = obj.find_entities(obj, start, end)
        elif start:
            response = obj.find_entities_starting_with(obj, start)
        elif end:
            response = obj.find_entities_starting_with(obj, end)
        else:
            response = obj.get_all_entities(obj)

        if isinstance(response, list) and len(response) != 0:
            return [item.as_dict() for item in response]
        elif isinstance(response, list) and len(response) == 0:
            return status404
        elif response:
            return response.as_dict()
        else:
            return status404

    @staticmethod
    def post(obj: CRUD, data, args):
        try:
            obj.update(obj(dict_as_data(args, data())))
        except IntegrityError:
            return status400

        return status200

    @staticmethod
    def delete(obj: CRUD, id):
        if entity := obj.find_entity(obj, id):
            obj.delete(entity)
            return status200

        return status404

    @staticmethod
    def patch(obj: CRUD, data, id: int, attr: str, value: str):
        if attr not in vars(data()).keys():
            return status400
        if entity := obj.find_entity(obj, id):
            entity.__setattr__(attr, value)
            entity.update(entity)
            return status200

        return status404
