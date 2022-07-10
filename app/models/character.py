from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from app.extensions import db
from app.models.utils import CRUD


class Character(CRUD, db.Model):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    rarity = Column(Integer)
    name_en = Column(String, unique=True, nullable=False)
    full_name = Column(String)
    card = Column(String)
    weapon = Column(String)
    eye = Column(String(16))
    sex = Column(String(16))
    birthday = Column(String(16))
    region = Column(String)
    affiliation = Column(String)
    portrait = Column(String)
    description = Column(String)
    modified_at: Column = Column(TIMESTAMP, default=current_timestamp(), onupdate=current_timestamp())
    created_at = Column(TIMESTAMP, default=current_timestamp(), nullable=False)

    wish_5 = relationship("WishCharacterFiveAssociation", back_populates="character", uselist=False)
    wish_4 = relationship("WishCharacterFourAssociation", back_populates="character")
