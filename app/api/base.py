from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import IntegrityError

from app.models.utils import CRUD
from app.utils.funcs import dict_as_data
from app.utils.datas import *
from flask import Response

status404 = Response("Not found", status=404)
status401 = Response("Not authorized", status=401)
status400 = Response("Bad request", status=400)
status200 = Response("Ok", status=200)


class BaseResource:
    @staticmethod
    def get(obj: CRUD, args: GET):
        if args.id is not None:
            response = obj.find_entity(obj, id)
        elif args.start is not None and args.end is not None:
            response = obj.find_entities(obj, start, end)
        elif args.start is not None:
            response = obj.find_entities_starting_with(obj, start)
        elif args.end is not None:
            response = obj.find_entities_ending_with(obj, end)
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
    def post(obj: CRUD, args):
        try:
            obj.update(obj(args))
        except IntegrityError:
            return status400

        return status200

    @staticmethod
    def delete(obj: CRUD, args: DELETE):
        if (entity := obj.find_entity(obj, args.id)) is not None:
            obj.delete(entity)
            return status200

        return status404

    @staticmethod
    def patch(obj: CRUD, data, args: PATCH):
        if args.attr not in vars(data()).keys():
            return status400
        if (entity := obj.find_entity(obj, args.id)) is not None:
            entity.__setattr__(args.attr, args.value)
            entity.update(entity)
            return status200

        return status404
