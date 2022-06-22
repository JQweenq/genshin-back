from flask_restful import Resource, reqparse
from app.data import WordData
from app.tables import Word
from app.api.base import BaseResource

getParser: reqparse.RequestParser = reqparse.RequestParser()

getParser.add_argument('from', type=int)
getParser.add_argument('to', type=int)
getParser.add_argument('id', type=int)

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('word', type=str)
postParser.add_argument('translate', type=str)
postParser.add_argument('subinf', type=str)
postParser.add_argument('original', type=str)

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

patchParser: reqparse.RequestParser = reqparse.RequestParser()

patchParser.add_argument('id', type=int, required=True)
patchParser.add_argument('attr', type=str, required=True)
patchParser.add_argument('value', type=str, required=True)


class Dictionary(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = getParser.parse_args()

        return BaseResource.get(Word, args['id'], args['from'], args['to'])

    @staticmethod
    def post() -> (dict, int):
        args = postParser.parse_args()

        return BaseResource.post(Word, WordData, args)

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        return BaseResource.delete(Word, args['id'])

    @staticmethod
    def patch():
        args: dict = patchParser.parse_args()

        return BaseResource.patch(Word, WordData, args['id'], args['attr'], args['value'])
