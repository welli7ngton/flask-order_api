# flake8: noqa

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
        'id': 3,
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
    assert len(response.json['items']) == 3
    assert response.json['items'][2]['id'] == obj['id']
    assert response.json['items'][2]['description'] == obj['description']
    assert response.json['items'][2]['price'] == obj['price']


def test_post_invalid_id(test_client):
    obj = {
        'description': 'teste id inválido',
        'price': 100.0
    }

    response = test_client.post(
        '/purchase_orders/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['id'] == 'Informe um ID.'


def test_post_invalid_description(test_client):
    obj = {
        'id': '2',
        'price': 100.0
    }

    response = test_client.post(
        '/purchase_orders/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição.'


def test_post_invalid_price(test_client):
    obj = {
        'id': '2',
        'description': 'Informe um preço.'
    }

    response = test_client.post(
        '/purchase_orders/1/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Informe um preço.'

def test_post_purchase_order_not_found(test_client):
    _id = 999
    obj = {
        'id': 3,
        'description': 'Novo Item',
        'price': 10000.00
    }

    response = test_client.post(
        f'/purchase_orders/{_id}/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.json == {'message': f'itens do pedido {_id} nao encontrados.'}