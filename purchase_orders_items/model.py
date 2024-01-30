# flake8:noqa
from db import DB


class PurchaseOrdersItemsModel(DB.Model):
    __tablename__ = 'purchase_order_items'

    id = DB.Column(DB.Integer, primary_key=True)
    description = DB.Column(DB.String(500), nullable=False)
    price = DB.Column(DB.Float(precision=2), nullable=False)
    purchase_order_id = DB.Column(DB.Integer, DB.ForeignKey('purchase_order.id'), nullable=False)
    quantity = DB.Column(DB.Integer, DB.ForeignKey('purchase_order.id'), nullable=False)

    def __init__(self, description, price, purchase_order_id, quantity) -> None:
        self.description = description
        self.price = price
        self.purchase_order_id = purchase_order_id
        self.quantity = quantity

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }
    
    @classmethod
    def find_by_purchase_order_id(cls, _purchase_order_id):
        return cls.query.filter_by(purchase_order_id=_purchase_order_id).all()
    
    def save(self):
        DB.session.add(self)
        DB.session.commit()
