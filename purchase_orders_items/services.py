# flake8:noqa
from purchase_orders_items.model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel
from flask import jsonify


class PurchaseOrderItemsService:
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
            purchase_order_item.save()

            return purchase_order_item.as_dict()
    
        return jsonify({'message': f'Itens do pedido {kwargs["purchase_order_id"]} não encontrados.'})