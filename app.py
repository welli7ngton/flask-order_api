from flask import Flask, jsonify

app = Flask(__name__)

purchase_order = [
    {
        'id': 1,
        'description': 'Pedido de compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 10.99,
            },
            {
                'id': 2,
                'description': 'Item do pedido 2',
                'price': 100.99,
            }
        ],
    },
]


@app.route('/')
def home():
    return 'Hello world'


@app.route('/purchase_orders')
def get_purchase_order():
    return jsonify(purchase_order)


app.run(port=5000)
