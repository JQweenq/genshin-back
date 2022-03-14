from flask_restful import Resource, reqparse
from app.tables import Wishe


getParser: reqparse.RequestParser = reqparse.RequestParser()

getParser.add_argument('from', type=int)
getParser.add_argument('to', type=int)
getParser.add_argument('id', type=int)

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('id', type=int, required=True)
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

        dictionary = Wishe.filter_table(Wishe, args)
        try:
            if len(dictionary) != 0:
                return [item.as_dict() for item in dictionary], 200
            return {
                       'message': 'do not found wishes'
                   }, 404
        except TypeError:
            if dictionary is not None:
                return dictionary.as_dict(), 200
            return {
                       'message': 'do not found wishes'
                   }, 404

    @staticmethod
    def post() -> (dict, int):
        args: dict = postParser.parse_args()
        try:
            Wishe.update(Wishe(args))
        except:
            return {
                       'message': 'do not created'
                   }, 400
        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        wishe = Wishe.query.filter(Wishe.id == args['id']).first()

        try:
            Wishe.delete(wishe)
        except:
            return {
                       'message': 'id do not found'
                   }, 404
        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def patch():
        args: dict = patchParser.parse_args()
        try:
            wishe = Wishe.query.filter(Wishe.id == args['id']).first()
            wishe.update_values(args)
            wishe.update(wishe)
            return {
                       'message': 'success'
                   }, 200
        except AttributeError:
            return {
                       'message': 'do not found id'
                   }, 200