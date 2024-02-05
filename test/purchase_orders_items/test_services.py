# flake8: noqa
import pytest
from purchase_orders_items.services import PurchaseOrderItemsService
from purchase_orders.exceptions import MaxQuantityException, MinQuantityException

def test_check_maximum_quantity(seed_db):
    with pytest.raises(MaxQuantityException) as ex:
        PurchaseOrderItemsService()._check_maximum_quantity(seed_db['purchase_orders'].id, seed_db['purchase_orders'].quantity, 51)
    assert ex.value.code == 400
    assert ex.value.description == 'Maximum quantity reached.'

def test_check_minimum_quantity(seed_db):
    with pytest.raises(MinQuantityException) as ex:
        PurchaseOrderItemsService()._check_minimum_quantity(seed_db['purchase_orders'].id, seed_db['purchase_orders'].quantity, 4)
    assert ex.value.code == 400
    assert ex.value.description == 'Minimum quantity not reached.'
