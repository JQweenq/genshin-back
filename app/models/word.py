from dataclasses import dataclass

from sqlalchemy import Column, String, TIMESTAMP, Integer
from sqlalchemy.sql.functions import current_timestamp

from app.extensions import db
from app.models.utils import CRUD


@dataclass()
class WordData:
    word: str = None
    translate: str = None
    subinf: str = None
    original: str = None


class Word(CRUD, db.Model):
    __tablename__ = 'dictionary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, unique=True, nullable=False)
    translate = Column(String)
    subinf = Column(String)
    original = Column(String)
    modified_at: Column = Column(TIMESTAMP, default=current_timestamp(), onupdate=current_timestamp())
    created_at = Column(TIMESTAMP, default=current_timestamp(), nullable=False)
