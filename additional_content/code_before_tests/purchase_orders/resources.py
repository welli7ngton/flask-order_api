from flask import jsonify
from flask_restful import Resource, reqparse


purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item 1 do pedido 1',
                'price': 10.99,
            },
            {
                'id': 2,
                'description': 'Item 2 do pedido 1',
                'price': 100.99,
            }
        ],
    },
]


class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Informe um ID válido.'
    )

    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição.'
    )

    def get(self):
        return jsonify(purchase_orders)

    def post(self):
        request_data = PurchaseOrders().parser.parse_args()
        purchase_order = {
            'id': request_data['id'],
            'description': request_data['description'],
            'items': []
        }

        purchase_orders.append(purchase_order)

        return jsonify(purchase_order)


class PurchaseOrdersById(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Informe um ID.'
    )

    def get(self, id):
        for purchase_order in purchase_orders:
            if purchase_order['id'] == id:
                return jsonify(purchase_order)
        return jsonify({'message': f'pedido {id} nao encontrado.'})
