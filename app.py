# flake8:noqa
from flask import Flask
from flask_restful import Api
from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrderItems
from db import DB


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lyz44fpc@localhost:5432/db_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrderItems, '/purchase_orders/<int:id>/items')

    @app.before_request
    def create_tables():
        DB.create_all()

    return app


# if __name__ == '__main__':
#     app = create_app()
#     app.run()
