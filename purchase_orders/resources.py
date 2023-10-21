from flask import jsonify
from flask_restful import Resource, reqparse
from purchase_object import purchase_order_obj


class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Verifique o ID.'
    )

    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição.'
    )

    def get(self):
        return jsonify(purchase_order_obj)

    def post(self):
        request_data = PurchaseOrders().parser.parse_args()
        purchase_order = {
            'id': request_data['id'],
            'description': request_data['description'],
            'items': []
        }

        purchase_order_obj.append(purchase_order)

        return jsonify(purchase_order)


class PurchaseOrdersById(Resource):
    def get(self, id):
        for purchase_order in purchase_order_obj:
            if purchase_order['id'] == id:
                return jsonify(purchase_order)
        return jsonify({'message': f'pedido {id} nao encontrado.'})
