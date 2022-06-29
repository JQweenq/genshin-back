from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse

from app.models.meta import Meta, MetaData
from app.api.base import BaseResource, status404, status200, basePatchParser

parser = reqparse.RequestParser()

parser.add_argument('attr', type=str, required=True)

postParser = reqparse.RequestParser()

postParser.add_argument('attr', type=str, required=True)
postParser.add_argument('value', type=str, required=True)

patchParser = parser.copy()

patchParser.add_argument('value', type=str, required=True)


class MetaRoute(Resource):
    @staticmethod
    def get():
        args: dict = parser.parse_args()

        if not Meta.get_by_attr(Meta, args['attr']):
            return status404

        return Meta.get_by_attr(Meta, args['attr']).as_dict()

    @staticmethod
    # @jwt_required()
    def post():
        # current_user = get_jwt_identity()
        args = postParser.parse_args()

        return BaseResource.post(Meta, MetaData, args)

    @staticmethod
    # @jwt_required()
    def delete():
        # current_user = get_jwt_identity()
        args: dict = parser.parse_args()

        if entity := Meta.get_by_attr(Meta, args['attr']):
            Meta.delete(entity)
            return status200
        else:
            return status404

    @staticmethod
    # @jwt_required()
    def patch():
        # current_user = get_jwt_identity()
        args: dict = patchParser.parse_args()

        if entity := Meta.get_by_attr(Meta, args['attr']):
            entity.__setattr__('value', args['value'])
            entity.update(entity)
            return status200
        else:
            return status404
