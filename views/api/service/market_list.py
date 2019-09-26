import re

from flask import Blueprint, request
from flask_restful import Api, Resource
from mongoengine.queryset.visitor import Q

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
        market_name = list(request.json['market'].split())

        # for i in market_name:
        #     test = Market_Model.objects.search_text(i).order_by('$text_score')
        #
        #     for testing in test:
        #         print(testing['name'])

        find = []

        for m in market_name:
            find.append(re.compile('.*'+m+'.*'))

        try:
            a = find[1]
        except:
                for i in find:
                    name_markets = Market_Model.objects(Q(name=i) | Q(location=i)).all()
                    for j in name_markets:
                        print(j['name'])

        for i in find:
            name_markets = Market_Model.objects(Q(name = i) & Q(location = i)).all()
            for j in name_markets:
                print(j['name'])
        #
        #     market_list = {}
        #
        #     a = 0
        #
        #     for market in name_markets:
        #         print(market['name'])
        #         market_list[a] = {
        #             "name": market['name'],
        #             "location": market['location'],
        #             "phone": market['telephone_num']
        #         }
        #         a += 1
        #
        # return market_list, 201
