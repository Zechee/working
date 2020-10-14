from sqlalchemy import ForeignKey, func

from app import db
from .base_model import BaseModel


class Logitem(BaseModel):
    __tablename__ = 'logitems'

    id = db.Column(db.Integer, primary_key=True)
    work_hour = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    content = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Logitem).filter(
            Logitem.id == id
        ).first()