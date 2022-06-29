from flask import Flask

from app.config import config
from app.extensions import setup_extensions


def create_app(config_type: str) -> Flask:
    # create application
    app: Flask = Flask(__name__)
    # setup config
    app.config.from_object(config[config_type])
    # setup extensions
    setup_extensions(app)
    # install blueprints
    from app.main import main
    app.register_blueprint(main)
    from app.api import api
    app.register_blueprint(api, url_prefix='/api')
    config[config_type].init_app(app)
    return app
