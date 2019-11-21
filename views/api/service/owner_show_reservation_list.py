import random

from flask import Blueprint, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.market import Market_Model
from models.service.order import Orderlist_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/order-list/<market_id>')
class RegisterMarket(Resource):
    @jwt_required
    def get(self, market_id):
        res = []
        order_list = Orderlist_Model.objects(market_id = market_id).all()
        market = Market_Model.objects(market_id = market_id).first()

        if not get_jwt_identity() == market['owner_id']:
            abort(409)

        for order in order_list:
            menu_list = []
            for menu in order['order']:
                menu_list.append(
                    {
                        "menu_name":menu["name"],
                        "menu_price":menu['price']
                    })
            res.append(
                {
                    "order_time":order['order_time'],
                    "customer": order['customer_id'],
                    "menu_list": menu_list
                })

        return {
            "order_list": res
            }, 200