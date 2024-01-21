import pytest
from db import DB

from purchase_orders.model import PurchaseOrderModel
from purchase_orders_items.model import PurchaseOrdersItemsModel


@pytest.fixture()
def seed_db():
    po = PurchaseOrderModel('Purchase Order Teste', 50)
    DB.session.add(po)
    DB.session.commit()

    yield po


@pytest.fixture(scope='function', autouse=True)
def clear_db():
    DB.session.query(PurchaseOrdersItemsModel).delete()
    DB.session.query(PurchaseOrderModel).delete()
    DB.session.commit()
