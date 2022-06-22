from flask_restful import Resource, reqparse
from app.tables import Word

getParser: reqparse.RequestParser = reqparse.RequestParser()

getParser.add_argument('from', type=int)
getParser.add_argument('to', type=int)
getParser.add_argument('id', type=int)

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('word', type=str)
postParser.add_argument('translate', type=str)
postParser.add_argument('subinf', type=str)
postParser.add_argument('original', type=str)

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

patchParser: reqparse.RequestParser = reqparse.RequestParser()

patchParser.add_argument('id', type=int, required=True)
patchParser.add_argument('word', type=str)
patchParser.add_argument('translate', type=str)
patchParser.add_argument('subinf', type=str)
patchParser.add_argument('original', type=str)


class Dictionary(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: dict = getParser.parse_args()

        dictionary = Word.filter_table(Word, args)
        if len(dictionary) != 0:
            return [item.as_dict() for item in dictionary], 200
        elif len(dictionary) == 1:
            return dictionary.as_dict(), 200
        else:
            return {
                       'message': 'Words not found'
                   }, 404

    @staticmethod
    def post() -> (dict, int):
        args: dict = postParser.parse_args()
        try:
            Word.update(Word(args))
        except:
            return {
                       'message': 'Word not created'
                   }, 400
        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        word = Word.query.filter(Word.id == args['id']).first()

        try:
            Word.delete(word)
        except:
            return {
                       'message': 'Id not found'
                   }, 404
        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def patch():
        args: dict = patchParser.parse_args()
        try:
            word = Word.query.filter(Word.id == args['id']).first()
            word.update_values(args)
            word.update(word)
            return {
                       'message': 'Success'
                   }, 200
        except AttributeError:
            return {
                       'message': 'Id not found'
                   }, 200
