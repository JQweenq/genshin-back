from flask_restful import Resource, reqparse
from app.tables import Characters as CharactersDB

parser: reqparse.RequestParser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=True, help='id field cannot be blank.')


class Character(Resource):

    @staticmethod
    def post() -> (dict, int):
        args = parser.parse_args()
        character = CharactersDB.query.filter_by(id=args['id']).first()
        if character is not None:
            return character, 200
        return {
                   'message': 'Такой персонаж не найден.'
               }, 404
