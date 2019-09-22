import random

from flask import Blueprint, request
from flask_restful import Api, Resource

from models.service.market import Market_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/register-market')
class RegisterMarket(Resource):
    def post(self):
        register_name = request.json['name']
        register_loc = request.json['location']
        register_num = request.json['phone']


        finder = Market_Model.objects(location=register_loc).first()


        if finder is not None:
            return '', 409


        while True:
            uuid = random.randrange(11111, 99999)
            if Market_Model.objects(authid=uuid).first() is None:
                break


        Market_Model(
            name = register_name,
            location = register_loc,
            telephone_num = register_num,
            authid = uuid
        ).save()

        return '', 201