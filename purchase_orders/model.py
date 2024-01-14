# flake8:noqa
from db import DB


class PurchaseOrderModel(DB.Model):
    __tablename__ = 'purchase_order'

    id = DB.Column(DB.Integer, primary_key=True)
    description = DB.Column(DB.String(500), nullable=False)

    def __init__(self, description) -> None:
        self.description = description
    
    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }

    @classmethod
    def find_all(cls):
        return cls.query.all() # select * from purchase_order

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() # select * from purchase_order where id == _id

    def save(self):
        DB.session.add(self)
        DB.session.commit()
