from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models.utils import CRUD


class User(CRUD, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    hash = Column(String(128), nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    modified_at: Column = Column(TIMESTAMP, default=current_timestamp(), onupdate=current_timestamp())
    created_at = Column(TIMESTAMP, default=current_timestamp(), nullable=False)

    @property
    def password(self):
        raise AttributeError('"password" is not a readable attribute')

    @password.setter
    def password(self, password):
        self.hash = generate_password_hash(password)

    def verify_password(self, password) -> bool:
        return check_password_hash(self.hash, password)

    def is_administrator(self):
        return self.is_admin
