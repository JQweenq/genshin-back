from flask_restful import Resource
from app.tables import Dictionary as DictionaryDB


class Dictionary(Resource):

    @staticmethod
    def post() -> (dict, int):
        dictionary = DictionaryDB.query.filter_by()
        if dictionary is not None:
            return dictionary, 200
        return {
                   'message': 'Нам очень жаль.'
               }, 404
