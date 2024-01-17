from flask_restful import Resource, reqparse
from .services import PurchaseOrderSerice


class PurchaseOrders(Resource):
    __service__ = PurchaseOrderSerice()
    parser = reqparse.RequestParser()

    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição.'
    )

    parser.add_argument(
        'quantity',
        type=int,
        required=True,
        help='informe uma quantidade'
    )

    def get(self):
        return self.__service__.find_all()

    def post(self):
        request_data = PurchaseOrders().parser.parse_args()
        return self.__service__.create(**request_data)


class PurchaseOrdersById(Resource):
    __service__ = PurchaseOrderSerice()

    def get(self, id):
        return self.__service__.find_by_id(id)
