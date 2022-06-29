from flask_restful import Resource, reqparse
from app.models.weapon import Weapon, WeaponData
from app.api.base import BaseResource, baseGetParser, basePatchParser, baseDeleteParser

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('title', type=str, required=True)
postParser.add_argument('icon', type=str)
postParser.add_argument('rarity', type=int)
postParser.add_argument('damage', type=int)
postParser.add_argument('dest', type=str)


class WeaponsRoute(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = baseGetParser.parse_args()

        return BaseResource.get(Weapon, args['id'], args['start'], args['end'])

    @staticmethod
    def post() -> (dict, int):
        args = postParser.parse_args()

        return BaseResource.post(Weapon, WeaponData, args)

    @staticmethod
    def delete():
        args: dict = baseDeleteParser.parse_args()

        return BaseResource.delete(Weapon, args['id'])

    @staticmethod
    def patch():
        args: dict = basePatchParser.parse_args()

        return BaseResource.patch(Weapon, WeaponData, args['id'], args['attr'], args['value'])
