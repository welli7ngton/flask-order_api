from db import DB


class PurchaseOrderModel(DB.Model):
    __tablename__ = 'purchase_order'

    id = DB.Column(DB.Integer, primary_key=True)
    description = DB.Column(DB.String(500), nullable=False)

    def __init__(self, description) -> None:
        self.description = description
