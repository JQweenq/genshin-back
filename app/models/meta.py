from sqlalchemy.sql.functions import current_timestamp

from app.extensions import db
from app.models.utils import CRUD


class Meta(CRUD, db.Model):
    __tablename__ = 'meta'

    attr = db.Column(db.String, primary_key=True)
    value = db.Column(db.String, nullable=False)
    modified_at: db.Column = db.Column(db.TIMESTAMP, default=current_timestamp(), onupdate=current_timestamp())
    created_at = db.Column(db.TIMESTAMP, default=current_timestamp(), nullable=False)

    @staticmethod
    def get_by_attr(base, attr: str):
        return db.session.query(base).filter(base.attr == attr).first()
