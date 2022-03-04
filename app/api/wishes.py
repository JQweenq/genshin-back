from flask_restful import Resource, reqparse
from app.tables import Wishe

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

class Wishes(Resource):

    @staticmethod
    def get() -> (dict, int):
        wishes = Wishe.query.filter_by()
        if wishes is not None:
            return [item.as_dict() for item in wishes], 200
        return {
                   'message': 'Мы искали под каждым камнем, но для нас это, как игла в стоге сена.'
               }, 404

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        character = Wishe.query.filter(Wishe.id == args['id']).first()

        try:
            Wishe.delete(character)
        except:
            return {
                       'message': 'id do not found'
                   }, 404
        return {
                   'message': 'Success'
               }, 200