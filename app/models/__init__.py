from app.extensions import db
from app.models.utils import CRUD


class WishCharacterFiveAssociationData:
    character_id: int = 0
    wish_id: int = 0


class WishCharacterFiveAssociation(CRUD, db.Model):  # one to one
    __tablename__ = 'wish_character_five_association'

    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    wish_id = db.Column(db.Integer, db.ForeignKey('wishes.id'), primary_key=True)
    character = db.relationship("Character", back_populates="wish_5")
    wish = db.relationship("Wish", back_populates="character_5")


class WishCharacterFourAssociationData:
    character_id: int = 0
    wish_id: int = 0


class WishCharacterFourAssociation(CRUD, db.Model):  # many to many
    __tablename__ = 'wish_character_four_association'

    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    wish_id = db.Column(db.Integer, db.ForeignKey('wishes.id'), primary_key=True)
    character = db.relationship("Character", back_populates="wish_4")
    wish = db.relationship("Wish", back_populates="character_4")
