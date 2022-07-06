from flask_restful import Resource
from flask import request
from app.models.word import Word
from app.data_models.word import WordData
from app.api.base import BaseResource
from app.utils.datas import *


class DictionaryRoute(Resource):

    @staticmethod
    def get() -> (dict, int):
        args: GET = request.parse()

        return BaseResource.get(Word, args)

    @staticmethod
    def post() -> (dict, int):
        args: POST = request.parse(['word'])

        return BaseResource.post(Word, args)

    @staticmethod
    def delete():
        args: DELETE = request.parse(['id'])

        return BaseResource.delete(Word, args)

    @staticmethod
    def patch():
        args: PATCH = request.parse(['id', 'attr', 'value'])

        return BaseResource.patch(Word, WordData, args)
