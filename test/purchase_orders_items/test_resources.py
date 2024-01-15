# flake8: noqa

import json


def test_get_purchase_order_items(test_client, seed_db):
    response = test_client.get(f'/purchase_orders/{seed_db["purchase_order"].id}/items')

    assert response.status_code == 200
    assert response.json[0]['id'] == seed_db['items'].id
    assert response.json[0]['description'] == seed_db['items'].description
    assert response.json[0]['price'] == seed_db['items'].price
    


def test_get_purchase_orders_items_id_not_found(test_client):
    id = 9999
    response = test_client.get(f'/purchase_orders/{id}/items')

    assert response.json['message'] == f'itens do pedido {id} nao encontrados.'


def test_post_add_items_to_a_purchase_order(test_client, seed_db):
    obj = {
        'description': 'Novo Item',
        'price': 10000.00
    }

    response = test_client.post(
        f'/purchase_orders/{seed_db["purchase_order"].id}/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] is not None
    assert response.json['description'] == obj['description']
    assert response.json['price'] == obj['price']


def test_post_invalid_description(test_client, seed_db):
    obj = {
        'price': 100.0
    }

    response = test_client.post(
        f'/purchase_orders/{seed_db["purchase_order"].id}/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição.'


def test_post_invalid_price(test_client, seed_db):
    obj = {
        'description': 'Informe um preço.'
    }

    response = test_client.post(
        f'/purchase_orders/{seed_db["purchase_order"].id}/items',
        data=json.dumps(obj),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Informe um preço.'

def test_post_purchase_order_not_found(test_client):
    _id = 99999999
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