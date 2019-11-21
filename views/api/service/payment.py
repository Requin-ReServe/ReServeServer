import random

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.market import Market_Model
from models.service.order import Orderlist_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/payment/<order_uuid>')
class RegisterMarket(Resource):
    @jwt_required
    def post(self, order_uuid):
        finder = Orderlist_Model.objects(order_uuid = order_uuid).first()

        if finder is None:
            return abort(409)

        finder.delete()

        return '', 200