from flask import Flask, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

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
    def get(self):
        return jsonify(purchase_orders)


api.add_resource(PurchaseOrders, '/purchase_orders')

app.run(port=5000)
