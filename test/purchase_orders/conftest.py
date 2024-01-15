import pytest
from db import DB

from purchase_orders.model import PurchaseOrderModel


@pytest.fixture()
def seed_db():
    po = PurchaseOrderModel('Purchase Order Teste')
    DB.session.add(po)
    DB.session.commit()

    yield po


@pytest.fixture(scope='function', autouse=True)
def clear_db():
    DB.session.query(PurchaseOrderModel).delete()
    DB.session.commit()
