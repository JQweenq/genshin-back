from flask import request
from flask_restful import Resource
from app.models.character import Character
from app.data_models.character import CharacterData
from app.utils.datas import *
from app.api.base import BaseResource


class CharactersRoute(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: GET = request.parse()

        return BaseResource.get(Character, args)

    @staticmethod
    def post() -> (dict, int):
        args: POST = request.parse(['name'])

        return BaseResource.post(Character, args)

    @staticmethod
    def delete():
        args: DELETE = request.parse(['id'])

        return BaseResource.delete(Character, args)

    @staticmethod
    def patch():
        args: PATCH = request.parse(['id', 'attr', 'value'])

        return BaseResource.patch(Character, CharacterData, args)
