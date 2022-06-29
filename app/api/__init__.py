from flask import Blueprint
from flask_restful import Api

from app.api.auth import RegistrationRoute, LoginRoute, LogoutRoute
from app.api.characters import CharactersRoute
from app.api.dictionary import DictionaryRoute
from app.api.meta import MetaRoute
from app.api.weapons import WeaponsRoute
from app.api.wishes import WishesRoute

api: Blueprint = Blueprint('api', __name__)

rest: Api = Api(api)

rest.add_resource(RegistrationRoute, '/register')
rest.add_resource(LoginRoute, '/login')
rest.add_resource(LogoutRoute, '/logout')
rest.add_resource(CharactersRoute, '/characters')
rest.add_resource(DictionaryRoute, '/dictionary')
rest.add_resource(WishesRoute, '/wishes')
rest.add_resource(WeaponsRoute, '/weapons')
rest.add_resource(MetaRoute, '/meta')
