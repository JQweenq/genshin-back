from flask_restful import Resource
from app.tables import Gebets as GebetsDB


class Gebets(Resource):

    @staticmethod
    def post() -> (dict, int):
        gebets = GebetsDB.query.filter_by()
        if gebets is not None:
            return gebets, 200
        return {
                   'message': 'Мы искали под каждым камнем, но для нас это, как игла в стоге сена.'
               }, 404
