from flask_restful import Resource, reqparse
from app.tables import Wish
from app.data import WishData
from app.api.base import BaseResource

getParser: reqparse.RequestParser = reqparse.RequestParser()

getParser.add_argument('from', type=int)
getParser.add_argument('to', type=int)
getParser.add_argument('id', type=int)

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('name', type=str)
postParser.add_argument('version', type=str)
postParser.add_argument('poster', type=str)
postParser.add_argument('rate_5', type=int)
postParser.add_argument('rate_4', type=int)

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

patchParser: reqparse.RequestParser = reqparse.RequestParser()

patchParser.add_argument('id', type=int, required=True)
patchParser.add_argument('attr', type=str, required=True)
patchParser.add_argument('value', type=str, required=True)


class Wishes(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = getParser.parse_args()

        return BaseResource.get(Wish, args['id'], args['from'], args['to'])

    @staticmethod
    def post() -> (dict, int):
        args = postParser.parse_args()

        return BaseResource.post(Wish, WishData, args)

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        return BaseResource.delete(Wish, args['id'])

    @staticmethod
    def patch():
        args: dict = patchParser.parse_args()

        return BaseResource.patch(Wish, WishData, args['id'], args['attr'], args['value'])