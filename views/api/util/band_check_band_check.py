import random

from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.service.market import Market_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/util'


@api.resource('/token')
class RegisterMarket(Resource):
    @jwt_required
    def get(self):
        return {
            "identity":get_jwt_identity()
        }, 200