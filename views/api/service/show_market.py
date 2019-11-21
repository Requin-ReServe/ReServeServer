import random

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.market import Market_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/market/<market_uuid>')
class RegisterMarket(Resource):
    def get(self, market_uuid):
        uuid = market_uuid

        finder = Market_Model.objects(market_id = uuid).first()

        if finder is None:
            return abort(409)

        return {
            "market_id":uuid,
            "market_name":finder['name'],
            "menu":finder['menu']
               }, 201

    @jwt_required
    def post(self, market_uuid):
        uuid = market_uuid

        finder = Market_Model.objects(market_id = uuid).first()

        if not finder['owner_id'] == get_jwt_identity():
            abort(406)

        menu_name = request.json['menu_name']
        menu_price = request.json['menu_price']

        if menu_name == None or menu_price == None:
            abort(409)

        finder.menu.append(
            {
                'menu_name': menu_name,
                'menu_price': menu_price
            }
        )

        finder.save()

        return '', 201

    @jwt_required
    def delete(self, market_uuid):
        uuid = market_uuid

        finder = Market_Model.objects(market_id=uuid).first()

        if not finder['owner_id'] == get_jwt_identity():
            abort(406)

        menu_name = request.json['menu_name']

        for i in finder.menu:
            if i['menu_name'] == menu_name:
                i.delete()

        finder.save()

        return '', 201