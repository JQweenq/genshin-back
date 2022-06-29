import re

from flask import jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

from app.api.base import status200, status401, status400
from app.models.user import User, UserData
from app.utils import dict_as_data

regParser: reqparse.RequestParser = reqparse.RequestParser()

regParser.add_argument('username', type=str, required=True)
regParser.add_argument('email', type=str, required=True)
regParser.add_argument('password', type=str, required=True)

logParser: reqparse.RequestParser = reqparse.RequestParser()

logParser.add_argument('username', type=str)
logParser.add_argument('email', type=str)
logParser.add_argument('password', type=str, required=True)


class RegistrationRoute(Resource):

    @staticmethod
    def post() -> (dict, int):
        args: dict = regParser.parse_args()

        if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', args['email']):
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
        args = logParser.parse_args()

        if args['username']:
            user = User.query.filter(User.username == args['username']).first()
        elif args['email']:
            user = User.query.filter(User.email == args['email']).first()
        else:
            return status400

        if user and user.verify_password(args['password']):
            return jsonify(access_token=create_access_token(identity=args['username']))

        return status401


class LogoutRoute(Resource):
    @staticmethod
    def post() -> (dict, int):
        # TODO logout_user
        return status200
