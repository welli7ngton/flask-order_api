import json


def test_get_purchase_order_items(test_client):
    response = test_client.get('/purchase_orders/1/items')

    assert response.status_code == 200
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == 'Item 1 do pedido 1'
    assert len(response.json) == 2


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
