from flask_restful import Resource, reqparse
from app.data import CharacterData
from app.tables import Character
from app.api.base import BaseResource

getParser: reqparse.RequestParser = reqparse.RequestParser()

getParser.add_argument('from', type=int)
getParser.add_argument('to', type=int)
getParser.add_argument('id', type=int)

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('name', type=str, required=True)
postParser.add_argument('rarity', type=int)
postParser.add_argument('name_en', type=str)
postParser.add_argument('full_name', type=str)
postParser.add_argument('card', type=str)
postParser.add_argument('weapon', type=str)
postParser.add_argument('eye', type=str)
postParser.add_argument('sex', type=str)
postParser.add_argument('birthday', type=str)
postParser.add_argument('region', type=str)
postParser.add_argument('affiliation', type=str)
postParser.add_argument('portrait', type=str)
postParser.add_argument('description', type=str)

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

patchParser: reqparse.RequestParser = reqparse.RequestParser()

patchParser.add_argument('id', type=int, required=True)
patchParser.add_argument('attr', type=str, required=True)
patchParser.add_argument('value', type=str, required=True)


class Characters(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = getParser.parse_args()

        return BaseResource.get(Character, args['id'], args['from'], args['to'])

    @staticmethod
    def post() -> (dict, int):
        args = postParser.parse_args()

        return BaseResource.post(Character, CharacterData, args)

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        return BaseResource.delete(Character, args['id'])

    @staticmethod
    def patch():
        args: dict = patchParser.parse_args()

        return BaseResource.patch(Character, CharacterData, args['id'], args['attr'], args['value'])
