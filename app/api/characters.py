from flask import jsonify
from flask_restful import Resource
from app.tables import Characters as CharactersDB


class Characters(Resource):

    @staticmethod
    def post() -> (dict, int):
        characters = CharactersDB
        print(characters)
        if characters is not None:
            return jsonify({
                'id': characters.id,
                'name': characters.name,
                'rarity': characters.rarity,
                'edited': characters.edited,
                'created': characters.created,
                   }), 200
        return {
                   'message': 'Не найдено ни одного персонажа.'
               }, 404
