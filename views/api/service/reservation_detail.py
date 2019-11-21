import random

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.market import Market_Model
from models.service.order import Orderlist_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/reservation/<order_id>')
class RegisterMarket(Resource):
    @jwt_required
    def get(self, order_id):
        res = []

        order_list = Orderlist_Model.objects(order_uuid = order_id).first()
        market_name = Market_Model.objects(market_id = order_list['market_id']).first()

        if not get_jwt_identity() == order_list['customer_id']:
            abort(409)

        for order in order_list['order']:
            res.append(
                {
                    "menu_name":order["name"],
                    "menu_price":order['price']
                })

        return {
            "market_name": market_name['name'],
            "order_time": order_list['order_time'],
            "menu_list": res
            }, 200