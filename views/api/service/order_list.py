from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.order import Orderlist_Model
from models.service.market import Market_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'

@api.resource('/order-list')
class OrderList(Resource):
    def get(self):
        pass

    @jwt_required
    def post(self):
        pass

