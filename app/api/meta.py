# from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, abort
from flask_restful import Resource

from app.api.base import BaseResource
from app.models.meta import Meta
from app.utils.datas import *


class MetaRoute(Resource):
    @staticmethod
    def get():
        args: GET = request.parse()

        if (result := Meta.get_by_attr(Meta, args.attr)) is None:
            return abort(404)

        return result.as_dict(args.ignore)

    @staticmethod
    # @jwt_required()
    def post():
        # current_user = get_jwt_identity()
        args: POST = request.parse(['attr', 'value'])

        return BaseResource.post(Meta, args)

    @staticmethod
    # @jwt_required()
    def delete():
        # current_user = get_jwt_identity()
        args: DELETE = request.parse(['attr'])

        if entity := Meta.get_by_attr(Meta, args.attr):
            Meta.delete(entity)
            return Response(status=200)
        else:
            return abort(404)

    @staticmethod
    # @jwt_required()
    def patch():
        # current_user = get_jwt_identity()
        args: dict = request.parse(['attr', 'value'])

        if entity := Meta.get_by_attr(Meta, args.attr):
            entity.__setattr__('value', args.value)
            entity.update(entity)
            return Response(status=200)
        else:
            return abort(404)
