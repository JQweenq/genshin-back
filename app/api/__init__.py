from flask import Blueprint
from flask_restful import Api

from app.api.auth import Registration, Login
from app.api.characters import Characters
from app.api.dictionary import Dictionary
from app.api.wishes import Wishes

api: Blueprint = Blueprint('api', __name__)

rest: Api = Api(api)


rest.add_resource(Registration, '/register')
rest.add_resource(Login, '/login')
rest.add_resource(Characters, '/characters')
rest.add_resource(Dictionary, '/dictionary')
rest.add_resource(Wishes, '/wishes')
