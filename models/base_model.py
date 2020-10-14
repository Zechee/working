from app import db

class BaseModel(db.Model):

    __abstract__ = True

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }
    def __repr__(self):
        return str(self.as_dict())

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def get_columns(self):
        return {
            c.name for c in self.__table__.columns
        }