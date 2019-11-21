import random

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.market import Market_Model
from models.user.user_model import User_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/my-market')
class RegisterMarket(Resource):
    @jwt_required
    def get(self):
        res = []
        finder = Market_Model.objects(owner_id = get_jwt_identity()).all()

        user = User_Model.objects(id = get_jwt_identity()).first()

        if finder is None:
            abort(409)

        if user['user_type'] == 0:
            abort(409)

        for market in finder:
            res.append({
                        "name": market['name'],
                        "image": market['image'],
                        "location": market['location'],
                        "tel_num": market['telephone_num'],
                        "market_id": market['market_id']
                    })

        return {
            "markets":res
               }, 201

    @jwt_required
    def delete(self):
        delete_market_uuid = request.json['market_id']

        finder = Market_Model.objects(market_id=delete_market_uuid).first()

        if not get_jwt_identity() == finder['owner_id']:
            abort(409)

        finder.delete()

        return "", 200