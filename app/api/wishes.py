from app.api.base import BaseResource, status200, status400, status404
from app.models.character import Character
from app.models.wish import Wish
from app.data_models.wish import WishData
from app.utils.funcs import dict_as_data
from app.utils.datas import *
from flask import request

from flask_restful import Resource
from sqlalchemy.exc import IntegrityError


class WishesRoute(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: GET = request.parse()

        if args.id is not None:
            wishes = Wish.find_entity(Wish, args.id)
        elif args.start is not None and end is not None:
            wishes = Wish.find_entities(Wish, args.start, args.end)
        elif args.start is not None:
            wishes = Wish.find_entities_starting_with(Wish, args.start)
        elif args.end is not None:
            wishes = Wish.find_entities_starting_with(Wish, args.end)
        else:
            wishes = Wish.get_all_entities(Wish)

        if wishes is None:
            return status404

        if isinstance(wishes, list) and len(wishes) != 0:
            return [item.as_dict(args.ignore) for item in wishes]
        elif isinstance(wishes, list) and len(wishes) == 0:
            return status404
        elif wishes:
            return wishes.as_dict(args.ignore)
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
        args: POST = request.parse(['title'])

        entity = Wish(args)
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
        args: DELETE = request.parse(['id'])

        return BaseResource.delete(Wish, args)

    @staticmethod
    def patch():
        args: PATCH = request.parse(['id', 'attr', 'value'])

        return BaseResource.patch(Wish, WishData, args)
