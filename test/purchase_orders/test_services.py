import pytest
from purchase_orders.services import PurchaseOrderSerice
from purchase_orders.exceptions import (
    MaxQuantityException, MinQuantityException
)


@pytest.mark.nocleardb
def test_check_quantity_minimum():
    with pytest.raises(MinQuantityException) as ex:
        PurchaseOrderSerice()._check_quantity(30)
    assert ex.value.code == 400
    assert ex.value.description == 'A quantidade deve ser maior igual que 50.'


@pytest.mark.nocleardb
def test_check_quantity_maximum():
    with pytest.raises(MaxQuantityException) as ex:
        PurchaseOrderSerice()._check_quantity(160)
    assert ex.value.code == 400
    assert ex.value.description == 'A quantidade deve ser menor igual que 150.'
