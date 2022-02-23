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
    isAdmin: db.Column = db.Column(db.Boolean, nullable=False, default=False)  # admin
    created: db.Column = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(),
                                   nullable=False)  # created time

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

    __tablename__ = 'character'

    id: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameEN: db.Column = db.Column(db.String)
    fullName: db.Column = db.Column(db.String)
    card: db.Column = db.Column(db.BINARY)
    weapon: db.Column = db.Column(db.String)
    eye: db.Column = db.Column(db.String(8))
    sex: db.Column = db.Column(db.String(8))
    birthday: db.Column = db.Column(db.String(10))
    region: db.Column = db.Column(db.String)
    affiliation: db.Column = db.Column(db.String)
    portrait: db.Column = db.Column(db.BINARY)
    dest: db.Column = db.Column(db.String)


class Dictionary(db.Model, Model):
    __tablename__ = 'dictionary'

    id: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Gebets(db.Model, Model):
    __tablename__ = 'gebets'
    id: db.Column = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: db.Column = db.Column(db.String)
    version: db.Column = db.Column(db.String(8))
    poster: db.Column = db.Column(db.BINARY)


'''{
			"5star": null,
			"4star1": null,
			"4star2": null,
			"4star3": null,
			"_mby": "60d83b48636261c2fe000250",
			"_by": "60d83b48636261c2fe000250",
			"_modified": 1625822697,
			"_created": 1625819170,
			"_id": "60e808223862655b11000258",
			"ch5star": null,
			"ch4star1": null,
			"ch4star2": null,
			"ch4star3": null
		},'''