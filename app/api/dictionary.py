from flask_restful import Resource, reqparse
from app.tables import Word

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

class Dictionary(Resource):

    @staticmethod
    def get() -> (dict, int):
        dictionary = Word.query.filter().all()
        if dictionary is not None:
            return [item.as_dict() for item in dictionary], 200
        return {
                   'message': 'Нам очень жаль.'
               }, 404

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        character = Word.query.filter(Word.id == args['id']).first()

        try:
            Word.delete(character)
        except:
            return {
                       'message': 'id do not found'
                   }, 404
        return {
                   'message': 'Success'
               }, 200
