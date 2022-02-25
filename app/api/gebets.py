from flask_restful import Resource
from app.tables import Gebets as GebetsDB


class Gebets(Resource):

    @staticmethod
    def get() -> (dict, int):
        gebets = GebetsDB.query.filter_by()
        if gebets is not None:
            return [item.as_dict() for item in gebets], 200
        return {
                   'message': 'Мы искали под каждым камнем, но для нас это, как игла в стоге сена.'
               }, 404
