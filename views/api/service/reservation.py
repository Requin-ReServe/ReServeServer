import random

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.market import Market_Model
from models.service.order import Orderlist_Model
from models.user.user_model import User_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/reservation')
class RegisterMarket(Resource):
    @jwt_required
    def get(self):
        res = []

        order_list = Orderlist_Model.objects(customer_id = get_jwt_identity()).all()

        for order in order_list:
            res.append(
                {
                    "order_id":order['order_uuid'],
                    "market_name": Market_Model.objects(market_id = order['market_id']).first()['name'],
                    "main_menu":order['order'][0]['name']
                })

        return {
            "order_list": res
            }, 200

    @jwt_required
    def post(self):
        market_id = request.json['market_id']
        reserve_list = request.json['menu']
        finder = Market_Model.objects(market_id = market_id).first()


        if finder is None:
            return abort(409)

        while True:
            uuid = random.randrange(11111, 99999)
            if Orderlist_Model.objects(order_uuid=uuid).first() is None:
                break

        for Rmenu in reserve_list:
            flag = True
            for menu in finder['menu']:
                if Rmenu['name'] == menu['menu_name']:
                    flag = False

            if flag:
                abort(409)

        Sum = 0

        for s in reserve_list:
            Sum += s['price']

        user = User_Model.objects(id=get_jwt_identity()).first()

        if user['point'] < Sum:
            abort(409)

        user.update(
            point = user['point'] - Sum
        )

        user.save()

        owner = User_Model.objects(
            id = Market_Model.objects(market_id = market_id).first()['owner_id']).first()

        owner.update(
            point = owner['point'] + Sum
        )

        Orderlist_Model(
            order_uuid = uuid,
            market_id = market_id,
            customer_id = get_jwt_identity(),
            order = reserve_list
        ).save()

        return "", 200

    @jwt_required
    def delete(self):
        order_id = request.json['order_id']

        finder = Orderlist_Model.objects(order_uuid = order_id).first()

        if finder is None:
            abort(409)

        elif not finder['customer_id'] == get_jwt_identity():
            abort(409)

        finder.delete()

        return '', 201
