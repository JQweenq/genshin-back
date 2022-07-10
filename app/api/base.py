from flask import abort, Response
from sqlalchemy.exc import IntegrityError

from app.models.utils import CRUD
from app.utils.datas import *


class BaseResource:
    @staticmethod
    def get(obj: CRUD, args: GET):
        if args.id is not None:
            response = obj.find_entity(obj, args.id)
        elif args.start is not None and args.end is not None:
            response = obj.find_entities(obj, args.start, args.end)
        elif args.start is not None:
            response = obj.find_entities_starting_with(obj, args.start)
        elif args.end is not None:
            response = obj.find_entities_ending_with(obj, args.end)
        else:
            response = obj.get_all_entities(obj)

        if isinstance(response, list) and len(response) != 0:
            return [item.as_dict(args.ignore, args.only) for item in response]
        elif isinstance(response, list) and len(response) == 0:
            return abort(404)
        elif response:
            return response.as_dict(args.ignore, args.only)
        else:
            return abort(404)

    @staticmethod
    def post(obj: CRUD, args):
        try:
            obj.update(obj(args))
        except IntegrityError:
            return abort(400)

        return Response(status=200)

    @staticmethod
    def delete(obj: CRUD, args: DELETE):
        if (entity := obj.find_entity(obj, args.id)) is not None:
            obj.delete(entity)
            return Response(status=200)

        return abort(404)

    @staticmethod
    def patch(obj: CRUD, data, args: PATCH):
        if args.attr not in vars(data()).keys():
            return abort(400)
        if (entity := obj.find_entity(obj, args.id)) is not None:
            entity.__setattr__(args.attr, args.value)
            entity.update(entity)
            return Response(status=200)

        return abort(404)
