# flake8: noqa
from purchase_orders.model import PurchaseOrderModel
from flask import jsonify
from .exceptions import MaxQuantityException, MinQuantityException


class PurchaseOrderSerice:

    def _check_quantity(self, quantity):
        if quantity < 50:
            raise MinQuantityException('A quantidade deve ser maior igual que 50.')
        if quantity > 150:
            raise MaxQuantityException('A quantidade deve ser menor igual que 150.')

    def find_all(self):
        purchase_orders = PurchaseOrderModel.find_all()
        return [p.as_dict() for p in purchase_orders]

    def create(self, **kwargs):
        self._check_quantity(kwargs['quantity'])
        purchase_order = PurchaseOrderModel(**kwargs)
        purchase_order.save()

        return purchase_order.as_dict()

    def find_by_id(self, id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            return purchase_order.as_dict()
        return jsonify({'message': f'pedido {id} nao encontrado.'})
