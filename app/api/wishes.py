from flask_restful import Resource
from app.tables import Wishes as WishesDB


class Wishes(Resource):

    @staticmethod
    def get() -> (dict, int):
        wishes = WishesDB.query.filter_by()
        if wishes is not None:
            return [item.as_dict() for item in wishes], 200
        return {
                   'message': 'Мы искали под каждым камнем, но для нас это, как игла в стоге сена.'
               }, 404
