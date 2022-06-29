from flask_restful import Resource, reqparse
from app.models.word import Word, WordData
from app.api.base import BaseResource, baseGetParser, basePatchParser, baseDeleteParser

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('word', type=str)
postParser.add_argument('translate', type=str)
postParser.add_argument('subinf', type=str)
postParser.add_argument('original', type=str)


class DictionaryRoute(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = baseGetParser.parse_args()

        return BaseResource.get(Word, args['id'], args['start'], args['end'])

    @staticmethod
    def post() -> (dict, int):
        args = postParser.parse_args()

        return BaseResource.post(Word, WordData, args)

    @staticmethod
    def delete():
        args: dict = baseDeleteParser.parse_args()

        return BaseResource.delete(Word, args['id'])

    @staticmethod
    def patch():
        args: dict = basePatchParser.parse_args()

        return BaseResource.patch(Word, WordData, args['id'], args['attr'], args['value'])
