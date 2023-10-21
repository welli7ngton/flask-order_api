from flask import Flask, jsonify, request

app = Flask(__name__)

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
    {
        'id': 2,
        'description': 'Pedido de compra 2',
        'items': []
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


@app.route('/purchase_orders/<int:id>/items')
def get_purchase_items_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po['items'])

    return jsonify({'message': f'itens do pedido {id} nao encontrados.'})


@app.route('/purchase_orders/<int:id>/add_items', methods=['POST'])
def add_items_to_purchase_order(id):
    request_data = request.get_json()
    for po in purchase_orders:
        if po['id'] == id:
            po['items'].append(
                {
                    'id': request_data['id'],
                    'description': request_data['description'],
                    'price': request_data['price']
                }
            )
            return jsonify(po)
    return jsonify({'message': f'purchase order id({id}) não encotrado.'})


app.run(port=5000)
