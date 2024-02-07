# flake8:noqa
import os
from flask import Flask
from flask_restful import Api
from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems
from db import DB
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from users.resources import UserCreation, UserLogin


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI_TEST']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY_TEST']

    DB.init_app(app)
    Migrate(app, DB)

    JWTManager(app)

    @app.route('/')
    def home():
        return 'Hello World!'

    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')
    api.add_resource(UserCreation, '/users')
    api.add_resource(UserLogin, '/login')

    @app.before_request
    def create_tables():
        DB.create_all()

    return app
