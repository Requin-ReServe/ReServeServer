import random

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.market import Market_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/register-market')
class RegisterMarket(Resource):
    @jwt_required
    def post(self):
        register_name = request.json['name']
        register_loc = request.json['location']
        register_num = request.json['phone']

        owner_id = get_jwt_identity()


        finder = Market_Model.objects(location=register_loc).first()


        if finder is not None:
            return abort(409)


        while True:
            uuid = random.randrange(11111, 99999)
            if Market_Model.objects(market_id=uuid).first() is None:
                break


        Market_Model(
            owner_name = owner_id,
            name = register_name,
            location = register_loc,
            telephone_num = register_num,
            market_id = uuid
        ).save()

        return '', 201