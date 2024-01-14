# flake8:noqa
from flask import jsonify
from flask_restful import Resource, reqparse
from .model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel


class PurchaseOrdersItems(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição.',
    )

    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='Informe um preço.',
    )

    def get(self, id):
        purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(id)

        return [p.as_dict() for p in purchase_orders_items]

    def post(self, id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            request_data = PurchaseOrdersItems.parser.parse_args()
            request_data['purchase_order_id'] = id

            purchase_orders_item = PurchaseOrdersItemsModel(**request_data)
            purchase_orders_item.save()

            return purchase_orders_item.as_dict()

        return jsonify({'message': f'itens do pedido {id} nao encontrados.'})
