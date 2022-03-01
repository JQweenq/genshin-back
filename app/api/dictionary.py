from flask_restful import Resource
from app.tables import Word as DictionaryDB

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

class Dictionary(Resource):

    @staticmethod
    def get() -> (dict, int):
        dictionary = DictionaryDB.query.filter().all()
        if dictionary is not None:
            return [item.as_dict() for item in dictionary], 200
        return {
                   'message': 'Нам очень жаль.'
               }, 404

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        character = Character.query.filter(Character.id == args['id']).first()

        try:
            Character.delete(character)
        except:
            return {
                       'message': 'id do not found'
                   }, 404
        return {
                   'message': 'Success'
               }, 200
