from flask_restful import Resource, reqparse

from app.extensions import db
parser: reqparse.RequestParser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=True, help='id field cannot be blank.')

class Character(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        character = Characters.query.filter_by(id=args['id']).first()
        return 404