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

        find = list()
        market_list = dict()
        name_markets_list = list()
        real_markets_list = list()
        a = 0
        flag = False
        flag_num = 1

        for m in market_name:
            find.append(re.compile('.*'+m+'.*'))

        try:
            find[1]
        except:
            flag = True

        if flag:
            for i in find:
                name_markets = Market_Model.objects(Q(name=i) | Q(location=i)).all()
                for market in name_markets:
                    market_list[a] = {
                        "name": market['name'],
                        "location": market['location'],
                        "phone": market['telephone_num']
                    }
                    a += 1

            return market_list, 201
        else:
            for i in find:
                if not flag:
                    name_markets_list.append(Market_Model.objects(location = i).all())
                    flag_num += 1

                if not name_markets_list[0]:
                    del name_markets_list[0]
                    name_markets_list.append(Market_Model.objects(name = i).all())
                    flag_num += 1

                if flag:
                    if flag_num == 2:
                        for j in name_markets_list[0]:
                            real_markets_list.append(
                                Market_Model.objects(Q(market_id = j['market_id']
                                ) & Q(name=i)).all()
                            )

                    if flag_num == 3:
                        for j in name_markets_list[0]:
                            real_markets_list.append(
                                Market_Model.objects(Q(market_id = j['market_id']
                                ) & Q(location=i)).all()
                            )

                flag = True

            for return_market_list in real_markets_list:
                for market in return_market_list:
                    market_list[a] = {
                        "name": market['name'],
                        "location": market['location'],
                        "phone": market['telephone_num']
                    }

                    a += 1

        return market_list, 201
