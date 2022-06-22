from flask_restful import Resource, reqparse
from app.data import WeaponData
from app.tables import Weapon
from app.api.base import BaseResource

getParser: reqparse.RequestParser = reqparse.RequestParser()

getParser.add_argument('from', type=int)
getParser.add_argument('to', type=int)
getParser.add_argument('id', type=int)

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('title', type=str, required=True)
postParser.add_argument('icon', type=str)
postParser.add_argument('rarity', type=int)
postParser.add_argument('damage', type=int)
postParser.add_argument('dest', type=str)

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

patchParser: reqparse.RequestParser = reqparse.RequestParser()

patchParser.add_argument('id', type=int, required=True)
patchParser.add_argument('attr', type=str, required=True)
patchParser.add_argument('value', type=str, required=True)


class Weapons(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = getParser.parse_args()

        return BaseResource.get(Weapon, args['id'], args['from'], args['to'])

    @staticmethod
    def post() -> (dict, int):
        args = postParser.parse_args()

        return BaseResource.post(Weapon, WeaponData, args)

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        return BaseResource.delete(Weapon, args['id'])

    @staticmethod
    def patch():
        args: dict = patchParser.parse_args()

        return BaseResource.patch(Weapon, WeaponData, args['id'], args['attr'], args['value'])
