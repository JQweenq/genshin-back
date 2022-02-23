class Config:
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool
    DEBUG: bool
    PORT: int
    HOST: str


class Dev(Config):
    print('This app is in dev mode')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///temp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    PORT = 8080
    HOST = '127.0.0.1'

class Prod(Config):
    pass

config = {
    'dev': Dev,
    'prod': Prod
}