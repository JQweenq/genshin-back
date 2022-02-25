import datetime



class Config:
    __abstract__ = True

    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool
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
    PERMANENT_SESSION_LIFETIME: datetime.timedelta
    SESSION_REFRESH_EACH_REQUEST: bool
    USE_X_SENDFILE: bool
    SEND_FILE_MAX_AGE_DEFAULT: datetime.timedelta or int
    SERVER_NAME: str
    APPLICATION_ROOT: str
    PREFERRED_URL_SCHEME: str
    MAX_CONTENT_LENGTH: int
    JSON_AS_ASCII: bool
    JSON_SORT_KEYS: bool
    JSONIFY_PRETTYPRINT_REGULAR: bool
    JSONIFY_MIMETYPE: str
    TEMPLATES_AUTO_RELOAD: bool
    EXPLAIN_TEMPLATE_LOADING: bool
    MAX_COOKIE_SIZE: int


class Dev(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEV MODE')


class Test(Config):
    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN TEST MODE')


class Prod(Config):
    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN PROD MODE')

config = {
    'dev': Dev,
    'Test': Test,
    'prod': Prod
}
