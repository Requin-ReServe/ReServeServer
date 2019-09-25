from flask import Blueprint, request
from flask_restful import Api, Resource

from models.service.market import Market_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'

@api.resource('/market-list')
class MarketList(Resource):
    def get(self):
        markets = Market_Model.objects().all()

        market_list = {}

        a = 0
        for market in markets:
            market_list[a] = {
                "name":market['name'],
                "location":market['location'],
                "phone":market['telephone_num']
            }
            a += 1

        return market_list, 201


    def post(self):
        market_name = request.json['market']

        markets = Market_Model.objects.search_text(market_name).order_by('$text_score')

        market_list = {}

        a = 0
        for market in markets:
            market_list[a] = {
                "name": market['name'],
                "location": market['location'],
                "phone": market['telephone_num']
            }
            a += 1

        return market_list, 201
