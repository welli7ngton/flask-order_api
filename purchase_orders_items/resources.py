# flake8:noqa
from flask import jsonify
from flask_restful import Resource, reqparse
from .model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel
from .services import PurchaseOrderItemsService


class PurchaseOrdersItems(Resource):
    __service__ = PurchaseOrderItemsService()
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

    parser.add_argument(
        'quantity',
        type=int,
        required=True,
        help='Informe uma quantidade válida.',
    )

    def get(self, id):
        return self.__service__.find_by_purchase_order_id(id)

    def post(self, id):
        request_data = PurchaseOrdersItems.parser.parse_args()
        request_data['purchase_order_id'] = id
        return self.__service__.create(**request_data)
