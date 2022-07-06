from dataclasses import dataclass

from sqlalchemy import String, Column, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from app.extensions import db
from app.models.utils import CRUD


class Wish(CRUD, db.Model):
    __tablename__ = 'wishes'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    version = Column(String(8))
    poster = Column(String)
    modified_at: Column = Column(TIMESTAMP, default=current_timestamp(), onupdate=current_timestamp())
    created_at = Column(TIMESTAMP, default=current_timestamp(), nullable=False)

    character_5 = relationship("WishCharacterFiveAssociation", back_populates="wish", uselist=False)
    character_4 = relationship("WishCharacterFourAssociation", back_populates="wish")

    # rate_5 = relationship('Character', backref="characters_rate5",
    #                       secondary=rate_five_association)  # wish to character as one to one
    # rate_4 = relationship('Character',
    #                       secondary=rate_four_association,
    #                       backref='characters_rate4')
