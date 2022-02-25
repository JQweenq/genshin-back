from flask_restful import Resource
from app.tables import Dictionary as DictionaryDB


class Dictionary(Resource):

    @staticmethod
    def get() -> (dict, int):
        dictionary = DictionaryDB.query.filter().all()
        if dictionary is not None:
            return [item.as_dict() for item in dictionary], 200
        return {
                   'message': 'Нам очень жаль.'
               }, 404
