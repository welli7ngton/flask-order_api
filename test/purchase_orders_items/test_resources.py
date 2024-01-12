import json


def test_get_purchase_order_items(test_client):
    id = 1
    response = test_client.get(f'/purchase_orders/{id}/items')

    assert response.status_code == 200
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == f'Item 1 do pedido {id}'
    assert len(response.json) == 2


def test_get_purchase_orders_items_id_not_found(test_client):
    id = 9999
    response = test_client.get(f'/purchase_orders/{id}/items')

    assert response.json['message'] == f'itens do pedido {id} nao encontrados.'


def test_post_add_items_to_a_purchase_order(test_client):
    obj = {
        'id': 2,
        'description': 'Novo Item',
        'price': 10000.00
    }

    response = test_client.post(
        '/purchase_orders/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] == 1
    assert len(response.json['items']) == 2
    assert response.json['items'][1] == obj['id']
    assert response.json['items'][1] == obj['description']
    assert response.json['items'][1] == obj['price']
