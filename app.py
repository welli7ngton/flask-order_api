# flake8:noqa
from flask import Flask
from flask_restful import Api
from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems
from db import DB
from flask_migrate import Migrate


def create_app(env='development'):
    app = Flask(__name__)
    api = Api(app)

    database = 'db_api'
    if env == 'testing':
        database = 'db_api_test'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:a@localhost:5432/{database}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)
    Migrate(app, DB)

    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')

    @app.before_request
    def create_tables():
        DB.create_all()

    return app
