from flask_restful import Resource
from flask import request
from app.models.weapon import Weapon
from app.data_models.weapon import WeaponData
from app.api.base import BaseResource
from app.utils.datas import *


class WeaponsRoute(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: GET = request.parse_args()

        return BaseResource.get(Weapon, args)

    @staticmethod
    def post() -> (dict, int):
        args: POST = request.parse(['title'])

        return BaseResource.post(Weapon, WeaponData, args)

    @staticmethod
    def delete():
        args: DELETE = request.parse(['id'])

        return BaseResource.delete(Weapon, args)

    @staticmethod
    def patch():
        args: PATCH = request.parse(['id', 'attr', 'value'])

        return BaseResource.patch(Weapon, WeaponData, args)
