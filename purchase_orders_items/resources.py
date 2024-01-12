from flask import jsonify
from flask_restful import Resource, reqparse
from purchase_object import purchase_order_obj


class PurchaseOrderItems(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id',
        type=int,
        required=True,
        help='Informe um ID.',
    )

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
        for po in purchase_order_obj:
            if po['id'] == id:
                return jsonify(po['items'])

        return jsonify({'message': f'itens do pedido {id} nao encontrados.'})

    def post(self, id):
        request_data = PurchaseOrderItems.parser.parse_args()
        for po in purchase_order_obj:
            if po['id'] == id:
                po['items'].append(
                    {
                        'id': request_data['id'],
                        'description': request_data['description'],
                        'price': request_data['price']
                    }
                )
                return jsonify(po)
        return jsonify({'message': f'itens do pedido {id} nao encontrados.'})
