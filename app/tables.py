from app.extensions import db, bcrypt

class Model:

    @staticmethod
    def add(resource):
        db.session.add(resource)
        return db.session.commit()

    @staticmethod
    def delete(resource):
        db.session.delete(resource)
        return db.session.commit()

    @staticmethod
    def update(resource):
        db.session.add(resource)
        return db.session.commit()

class User(db.Model, Model):

    __tablename__: str = 'users'

    uid: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)  # uid
    token: db.Column = db.Column(db.String)  # token
    username: db.Column = db.Column(db.String, nullable=False)  # login
    password: db.Column = db.Column(db.String, nullable=False)  # password
    email: db.Column = db.Column(db.String, nullable=False, unique=True)  # email
    created: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)  # created time

    def __repr__(self) -> str:
        return '<User %r:%r>' % (self.uid, self.username)

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.hash, password)

    def hash_password(self, password: str) -> None:
        self.hash = bcrypt.generate_password_hash(password, 13).decode('ascii')

class Characters(db.Model, Model):

    __tablename__: str = 'characters'

    id: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: db.Column = db.Column(db.String)
    rarity: db.Column = db.Column(db.String)

    edited: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    created: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

class Character(db.Model, Model):
    pass

class Dictionary(db.Model, Model):
    pass

class Gebets(db.Model, Model):
    pass