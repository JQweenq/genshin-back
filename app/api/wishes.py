from app.api.base import BaseResource, baseGetParser, basePatchParser, baseDeleteParser, status200, status400, status404
from app.models.character import Character
from app.models.wish import Wish, WishData
from app.utils import dict_as_data

from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('title', type=str)
postParser.add_argument('version', type=str)
postParser.add_argument('poster', type=str)
postParser.add_argument('rate_5', type=int)
postParser.add_argument('rate_4', type=int, action='append')


class WishesRoute(Resource):

    @staticmethod
    def get() -> (dict, int):
        args = baseGetParser.parse_args()

        id = args['id']
        start = args['start']
        end = args['end']

        if id:
            wishes = [Wish.find_entity(Wish, id)]
        elif start and end:
            wishes = Wish.find_entities(Wish, start, end)
        elif start:
            wishes = Wish.find_entities_starting_with(Wish, start)
        elif end:
            wishes = Wish.find_entities_starting_with(Wish, end)
        else:
            wishes = Wish.get_all_entities(Wish)

        if wishes == [] or not wishes:
            return status404

        if isinstance(wishes, list) and len(wishes) != 0:
            return [item.as_dict() for item in wishes]
        elif isinstance(wishes, list) and len(wishes) == 0:
            return status404
        elif wishes:
            return wishes.as_dict()
        else:
            return status404

        # for wish in wishes:
        #     wish_dict: dict = wish.as_dict()
        #     rate_4_dict = {
        #         'rate_4': [{rate_4.character_id: Character.find_entity(Character, rate_4.character_id).name} for rate_4
        #                    in Wish.db.session.query(rate_four_association).filter(rate_four_association.c.wishes_id == wish.id).all()]}
        #
        #     if row := Wish.db.session.query(rate_five_association).filter(rate_five_association.c.wishes_id == wish.id).first():
        #         rate5_dict = {'rate_5': {row.character_id: Character.find_entity(Character, row.character_id).name}}
        #     else:
        #         rate5_dict = {'rate_5': {}}
        #
        #     wish_dict.update(rate_4_dict)
        #     wish_dict.update(rate5_dict)
        #     list_wishes.append(wish_dict)

    @staticmethod
    def post() -> (dict, int):
        args = postParser.parse_args()

        rate5 = args.pop('rate_5')
        rate4 = args.pop('rate_4')

        entity = Wish(dict_as_data(args, WishData()))
        # todo create relationship
        # if not rate5:
        #     if character5 := Character.query.filter(Character.id == rate5).first():
        #         entity.rate_5 = character5
        #     else:
        #         return status404
        # if not rate4:
        #     for rate in rate4:
        #         if character4 := Character.query.filter(Character.id == rate).first():
        #             entity.rate_4.append(character4)
        #         else:
        #             return status404

        try:
            Wish.update(entity)
        except IntegrityError:
            return status400
        return status200

    @staticmethod
    def delete():
        args: dict = baseDeleteParser.parse_args()

        return BaseResource.delete(Wish, args['id'])

    @staticmethod
    def patch():
        args: dict = basePatchParser.parse_args()

        return BaseResource.patch(Wish, WishData, args['id'], args['attr'], args['value'])
