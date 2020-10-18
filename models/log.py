from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Log(BaseModel):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Log).filter(
            Log.id == id
        ).first()