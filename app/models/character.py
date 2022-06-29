from dataclasses import dataclass

from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from app.extensions import db
from app.models.utils import CRUD


@dataclass()
class CharacterData:
    name: str = None
    rarity: int = None
    name_en: str = None
    full_name: str = None
    card: str = None
    weapon: str = None
    eye: str = None
    sex: str = None
    birthday: str = None
    region: str = None
    affiliation: str = None
    portrait: str = None
    description: str = None


class Character(CRUD, db.Model):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    rarity = Column(Integer)
    name_en = Column(String)
    full_name = Column(String)
    card = Column(String)
    weapon = Column(String)
    eye = Column(String(8))
    sex = Column(String(8))
    birthday = Column(String(10))
    region = Column(String)
    affiliation = Column(String)
    portrait = Column(String)
    description = Column(String)
    modified_at: Column = Column(TIMESTAMP, default=current_timestamp(), onupdate=current_timestamp())
    created_at = Column(TIMESTAMP, default=current_timestamp(), nullable=False)

    wish_5 = relationship("WishCharacterFiveAssociation", back_populates="character", uselist=False)
    wish_4 = relationship("WishCharacterFourAssociation", back_populates="character")

    # rate_5 = relationship('Wish', secondary=rate_five_association, backref="wish_rate%5")  # character to wish as many to many
    # rate_4 = relationship('Wish', secondary=rate_four_association,
    #                       backref='wishes_rate4')  # wish to characters as many to many
