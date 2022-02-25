from flask import jsonify
from flask_restful import Resource
from app.tables import Characters as CharactersDB


class Characters(Resource):

    @staticmethod
    def get() -> (dict, int):
        characters: list = CharactersDB.query.filter()
        if characters is not None:
            return [item.as_dict() for item in characters], 200
        return {
                   'message': 'Не найдено ни одного персонажа.'
               }, 404