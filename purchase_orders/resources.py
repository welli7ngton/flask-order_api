from flask import jsonify
from flask_restful import Resource
from purchase_object import purchase_order_obj


class PurchaseOrders(Resource):

    def get(self):
        return jsonify(purchase_order_obj)
