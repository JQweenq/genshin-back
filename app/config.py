import os

class Config:
    __abstract__ = True

    SQLALCHEMY_ECHO: bool = False
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    ENV: str
    DEBUG: bool
    TESTING: bool
    PROPAGATE_EXCEPTIONS: bool
    PRESERVE_CONTEXT_ON_EXCEPTION: bool
    TRAP_HTTP_EXCEPTIONS: bool
    TRAP_BAD_REQUEST_ERRORS: bool
    SECRET_KEY: bytes or str
    SESSION_COOKIE_NAME: str
    SESSION_COOKIE_DOMAIN: bool
    SESSION_COOKIE_PATH: str
    SESSION_COOKIE_HTTPONLY: bool
    SESSION_COOKIE_SECURE: bool
    SESSION_COOKIE_SAMESITE: str
    SESSION_REFRESH_EACH_REQUEST: bool
    USE_X_SENDFILE: bool
    SERVER_NAME: str
    APPLICATION_ROOT: str
    PREFERRED_URL_SCHEME: str
    MAX_CONTENT_LENGTH: int
    JSON_AS_ASCII: bool
    JSON_SORT_KEYS: bool = False
    JSONIFY_PRETTYPRINT_REGULAR: bool
    JSONIFY_MIMETYPE: str
    TEMPLATES_AUTO_RELOAD: bool
    EXPLAIN_TEMPLATE_LOADING: bool
    MAX_COOKIE_SIZE: int
    JWT_SECRET_KEY: str = 'admin'


class Dev(Config):
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'admin'
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEV MODE')
        print(app.url_map)


class Test(Config):
    SECRET_KEY = 'admin'
    TESTING = True

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN TEST MODE')
        print(app.url_map)


class Prod(Config):
    """UNIX OS"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///database.db')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'admin')
    SECRET_KEY = os.getenv('SECRET_KEY', 'admin')

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN PROD MODE')


config = {
    'dev': Dev,
    'test': Test,
    'prod': Prod
}
