# flake8:noqa
from purchase_orders_items.model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel
from flask import jsonify
from purchase_orders.exceptions import MaxQuantityException, MinQuantityException


class PurchaseOrderItemsService:
    def _check_maximum_quantity(self, quantity):
        if quantity > 50:
            raise MaxQuantityException('Maximum quantity reached.')

    def _check_minimum_quantity(self, quantity):
        if quantity < 5:
            raise MinQuantityException('Minimum quantity not reached.')

    def find_by_purchase_order_id(self, purchase_order_id):
        purchase_order = PurchaseOrderModel.find_by_id(purchase_order_id)
        if purchase_order:
            purchase_order_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(purchase_order_id)

            return [p.as_dict() for p in purchase_order_items]
        return jsonify({'message': f'itens do pedido {purchase_order_id} nao encontrados.'})
    
    def create(self, **kwargs):
        purchase_order = PurchaseOrderModel.find_by_id(kwargs['purchase_order_id'])
        if purchase_order:
            purchase_order_item = PurchaseOrdersItemsModel(**kwargs)
            self._check_maximum_quantity(purchase_order_item.quantity)
            self._check_minimum_quantity(purchase_order_item.quantity)

            purchase_order_item.save()

            return purchase_order_item.as_dict()
    
        return jsonify({'message': f'Itens do pedido {kwargs["purchase_order_id"]} não encontrados.'})
