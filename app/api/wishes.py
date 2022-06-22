from flask_restful import Resource, reqparse
from app.tables import Wish

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
patchParser.add_argument('name', type=str)
patchParser.add_argument('version', type=str)
patchParser.add_argument('poster', type=str)
patchParser.add_argument('rate_5', type=int)
patchParser.add_argument('rate_4', type=int)


class Wishes(Resource):
    @staticmethod
    def get() -> (dict, int):
        args: dict = getParser.parse_args()

        dictionary = Wish.filter_table(Wish, args)
        if len(dictionary) != 0:
            return [item.as_dict() for item in dictionary], 200
        elif len(dictionary) == 1:
            return dictionary.as_dict(), 200
        else:
            return {
                       'message': 'Wishes not found'
                   }, 404

    @staticmethod
    def post() -> (dict, int):
        args: dict = postParser.parse_args()
        try:
            Wish.update(Wish(args))
        except:
            return {
                       'message': 'Wish not created'
                   }, 400
        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        wish = Wish.query.filter(Wish.id == args['id']).first()

        try:
            Wish.delete(wish)
        except:
            return {
                       'message': 'Id not found'
                   }, 404
        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def patch():
        args: dict = patchParser.parse_args()
        try:
            wishe = Wish.query.filter(Wish.id == args['id']).first()
            wishe.update_values(args)
            wishe.update(wishe)
            return {
                       'message': 'Success'
                   }, 200
        except AttributeError:
            return {
                       'message': 'Id not found'
                   }, 200
