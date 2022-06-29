from flask_restful import Resource, reqparse
from app.models.character import Character, CharacterData
from app.api.base import BaseResource, baseGetParser, basePatchParser, baseDeleteParser

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


class CharactersRoute(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = baseGetParser.parse_args()

        return BaseResource.get(Character, args['id'], args['start'], args['end'])

    @staticmethod
    def post() -> (dict, int):
        args = postParser.parse_args()

        return BaseResource.post(Character, CharacterData, args)

    @staticmethod
    def delete():
        args: dict = baseDeleteParser.parse_args()

        return BaseResource.delete(Character, args['id'])

    @staticmethod
    def patch():
        args: dict = basePatchParser.parse_args()

        return BaseResource.patch(Character, CharacterData, args['id'], args['attr'], args['value'])
