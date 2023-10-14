from flask import Flask, jsonify, request

app = Flask(__name__)

purchase_orders = [
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
    {
        'id': 2,
        'description': 'Pedido de compra 2',
        'items': False
    }
]


@app.route('/')
def home():
    return 'Hello world'


@app.route('/purchase_orders')
def get_purchase_order():
    return jsonify(purchase_orders)


@app.route('/purchase_orders/<int:id>')
def get_purchase_order_by_id(id):
    for purchase_order in purchase_orders:
        if purchase_order['id'] == id:
            return jsonify(purchase_order)
    return jsonify({'message': f'pedido {id} nao encontrado.'})


@app.route('/purchase_orders', methods=['POST'])
def create_purchase_order():
    request_data = request.get_json()
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items': []
    }

    purchase_orders.append(purchase_order)

    return jsonify(purchase_order)


app.run(port=5000)
