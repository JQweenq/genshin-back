# from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import request

from app.models.meta import Meta
from app.data_models.meta import MetaData
from app.utils.datas import *
from app.api.base import BaseResource, status404, status200


class MetaRoute(Resource):
    @staticmethod
    def get():
        args: GET = request.parse()

        if (result := Meta.get_by_attr(Meta, args.attr)) is None:
            return status404

        return result.as_dict()

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
        args: DELETE = parser.parse_args(['attr'])

        if entity := Meta.get_by_attr(Meta, args.attr):
            Meta.delete(entity)
            return status200
        else:
            return status404

    @staticmethod
    # @jwt_required()
    def patch():
        # current_user = get_jwt_identity()
        args: dict = patchParser.parse_args(['attr', 'value'])

        if entity := Meta.get_by_attr(Meta, args.attr):
            entity.__setattr__('value', args.value)
            entity.update(entity)
            return status200
        else:
            return status404
