from flask_restful import Resource, reqparse
from app.tables import Word


getParser: reqparse.RequestParser = reqparse.RequestParser()

getParser.add_argument('from', type=int)
getParser.add_argument('to', type=int)
getParser.add_argument('one', type=int)

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
postParser.add_argument('portrait', type=bytes)
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


class Dictionary(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = getParser.parse_args()

        dictionary = Word.filter_table(Word, args)
        try:
          if len(dictionary) != 0:
            return [item.as_dict() for item in dictionary], 200
          return {
            'message': 'Не найдено ни одного word or dictionary.'
          }, 404
        except TypeError:
          return dictionary.as_dict(), 200

    @staticmethod
    def post():
      args: dict = postParser.parse_args()
      word = Word(_dict=args)
      try:
          Word.update(word)
          return {
            'message': 'Success'
          }, 200
      except:
          return {
            'message': 'do not updated'
          }, 400

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        word = Word.query.filter(Word.id == args['id']).first()

        try:
            Word.delete(word)
        except:
            return {
              'message': 'id do not found'
            }, 404
        return {
            'message': 'Success'
          }, 200
    
    @staticmethod
    def patch():
        '''not work yet'''
        args: dict = patchParser.parse_args()

        character = Character.query.filter(Character.id == args['id']).first()
        newCharacter = Character()
        character.update(newCharacter)

        return {
          'message': 'success'
        }, 200
