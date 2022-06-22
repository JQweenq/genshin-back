from app.tables import Base
from app.utils import dict_as_data


class BaseResource:
    @staticmethod
    def get(obj: Base, id=None, _from=None, to=None):
        response = obj.filter_table(obj, id, _from, to)

        if isinstance(response, list) and len(response) != 0:
            return [item.as_dict() for item in response], 200
        elif response is not None:
            return response.as_dict(), 200
        else:
            return 404

    @staticmethod
    def post(obj: Base, data, args):
        entity = obj(dict_as_data(args, data()))

        try:
            obj.update(entity)
        except:
            return 400
        return 200

    @staticmethod
    def delete(obj: Base, id):
        character = obj.query.filter(obj.id == id).first()

        try:
            obj.delete(character)
        except:
            return 404
        return 200

    @staticmethod
    def patch(obj: Base, data, id, attr, value):
        try:
            character = obj.query.filter(obj.id == id).first()
            character.__setattr__(attr, value)
            character.update(character)
            return 200
        except AttributeError:
            return 404
