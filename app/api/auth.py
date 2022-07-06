import re

from flask import jsonify, request
# from flask_jwt_extended import create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from app.api.base import status200, status401, status400
from app.models.user import User
from app.data_models.user import UserData
from app.utils.funcs import dict_as_data


class RegistrationRoute(Resource):

    @staticmethod
    def post() -> (dict, int):
        args: POST = request.parse(['username', 'email', 'password'])

        if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', args.email):
            return status400

        try:
            user = User(dict_as_data(args, UserData()))
            user.add(user)
            return status200
        except IntegrityError:
            return status400


class LoginRoute(Resource):

    @staticmethod
    def post() -> (dict, int):
        args: POST = request.parse(['password'])

        if args.username:
            user = User.query.filter(User.username == args.username).first()
        elif args.email:
            user = User.query.filter(User.email == args.email).first()
        else:
            return status400

        if user and user.verify_password(args.password):
            return status200
            # return jsonify(access_token=create_access_token(identity=args['username']))

        return status401


class LogoutRoute(Resource):
    @staticmethod
    def post() -> (dict, int):
        # TODO logout_user
        return status200
