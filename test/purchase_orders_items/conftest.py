import pytest
from db import DB

from purchase_orders_items.model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel


@pytest.fixture()
def seed_db():
    po = PurchaseOrderModel('Pedido de testes', 50)
    DB.session.add(po)
    DB.session.commit()

    poi = PurchaseOrdersItemsModel("Item teste - 1", 50.00, po.id, 10)
    DB.session.add(poi)
    DB.session.commit()

    yield {'purchase_order': po, 'items': poi}


@pytest.fixture(scope='function', autouse=True)
def clear_db():
    DB.session.query(PurchaseOrdersItemsModel).delete()
    DB.session.query(PurchaseOrderModel).delete()
