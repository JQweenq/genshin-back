from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

from app.tables import User



regParser: reqparse.RequestParser = reqparse.RequestParser()

regParser.add_argument('username', type=str, required=True, help='Username field cannot be blank.')
regParser.add_argument('email', type=str, required=True, help='Email field cannot be blank.')
regParser.add_argument('password', type=str, required=True, help='Password field cannot be blank.')

logParser: reqparse.RequestParser = reqparse.RequestParser()

logParser.add_argument('email', type=str, required=True, help='Email field cannot be blank.')
logParser.add_argument('password', type=str, required=True, help='Password field cannot be blank.')


class Registration(Resource):

    @staticmethod
    def post() -> (dict, int):
        args: dict = regParser.parse_args()

        try:
            user = User(args)
            user.password = args['password']
            user.add(user)
            return {
                       'message': 'Аккаунт создан'
                   }, 200
        except IntegrityError:
            return {
                       'message': 'Такой пользователь уже существует'
                   }, 401

class Login(Resource):

    @staticmethod
    def post() -> (dict, int):
        args = logParser.parse_args()

        user = User.query.filter(User.email == args['email']).first()

        if user is not None and \
                user.verify_password(args['password']):
            return {
                       'message': 'Успешно авторизирован',
                       'id': user.id,
                       'created': user.created_at.strftime('%m/%d/%Y, %H:%M:%S'),
                       'username': user.username
                   }, 200
        return {
                   'message': 'Введен не правильный логин или пароль'
               }, 401
