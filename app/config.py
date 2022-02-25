class Config:
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool
    DEBUG: bool
    PORT: int
    HOST: str


class Dev(Config):
    print('This app is in dev mode')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class Prod(Config):
    pass

config = {
    'dev': Dev,
    'prod': Prod
}