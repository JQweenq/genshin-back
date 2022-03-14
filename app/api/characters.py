from flask_restful import Resource, reqparse
from app.tables import Character

getParser: reqparse.RequestParser = reqparse.RequestParser()

getParser.add_argument('from', type=int)
getParser.add_argument('to', type=int)
getParser.add_argument('id', type=int)

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('id', type=int)
postParser.add_argument('name', type=str)
postParser.add_argument('rarity', type=int)
postParser.add_argument('name_en', type=str)
postParser.add_argument('full_name', type=str)
postParser.add_argument('card', type=str)
postParser.add_argument('weapon', type=str)
postParser.add_argument('eye', type=str)
postParser.add_argument('sex', type=str)
postParser.add_argument('birthday', type=int)
postParser.add_argument('region', type=str)
postParser.add_argument('affiliation', type=str)
postParser.add_argument('portrait', type=str)
postParser.add_argument('description', type=str)

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

patchParser: reqparse.RequestParser = reqparse.RequestParser()

patchParser.add_argument('id', type=int, required=True)
patchParser.add_argument('name', type=str)
patchParser.add_argument('rarity', type=int)
patchParser.add_argument('name_en', type=str)
patchParser.add_argument('full_name', type=str)
patchParser.add_argument('card', type=str)
patchParser.add_argument('weapon', type=str)
patchParser.add_argument('eye', type=str)
patchParser.add_argument('sex', type=str)
patchParser.add_argument('birthday', type=int)
patchParser.add_argument('region', type=str)
patchParser.add_argument('affiliation', type=str)
patchParser.add_argument('portrait', type=bytes)
patchParser.add_argument('description', type=str)


class Characters(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = getParser.parse_args()

        characters = Character.filter_table(Character, args)
        try:
            if len(characters) != 0:
                return [item.as_dict() for item in characters], 200
            return {
                'message': 'Не найдено ни одного персонажа.'
            }, 404
        except TypeError:
            if characters is not None:
                return characters.as_dict(), 200
            return {
                'message': 'Не найдено ни одного персонажа.'
            }, 404
        

    @staticmethod
    def post() -> (dict, int):
        args: dict = postParser.parse_args()
        character = Character(args)
        try:
            Character.update(character)
        except:
            return {
              'message': 'do not created'
            }, 400
        return {
          'message': 'Success'
        }, 200

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        character = Character.query.filter(Character.id == args['id']).first()

        try:
            Character.delete(character)
        except:
            return {
                       'message': 'id do not found'
                   }, 404
        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def patch():
        args: dict = patchParser.parse_args()
        try:
            character = Character.query.filter(Character.id == args['id']).first()
            character.update_values(args)
            character.update(character)
            return {
                'message': 'success'
            }, 200
        except AttributeError:
            return {
                'message': 'do not found id'
            }, 200