from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp

from app.extensions import db
from app.models.utils import CRUD


class Weapon(CRUD, db.Model):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    title_en = Column(String, unique=True, nullable=False)
    icon = Column(String)
    rarity = Column(Integer)
    damage = Column(Integer)
    dest = Column(String)
    modified_at: Column = Column(TIMESTAMP, default=current_timestamp(), onupdate=current_timestamp())
    created_at = Column(TIMESTAMP, default=current_timestamp(), nullable=False)
