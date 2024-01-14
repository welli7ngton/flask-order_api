from flask import jsonify
from flask_restful import Resource, reqparse
from .model import PurchaseOrderModel


class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição.'
    )

    def get(self):
        purchase_orders = PurchaseOrderModel.find_all()
        return [p.as_dict() for p in purchase_orders]

    def post(self):
        request_data = PurchaseOrders().parser.parse_args()
        purchase_order = PurchaseOrderModel(**request_data)
        purchase_order.save()

        return purchase_order.as_dict()


class PurchaseOrdersById(Resource):
    def get(self, id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            return purchase_order.as_dict()
        return jsonify({'message': f'pedido {id} nao encontrado.'})
