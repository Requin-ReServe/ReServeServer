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

        find = list()
        market_list = dict()
        name_markets_list = list()
        a = 0
        b = 0
        flag = False
        return_market_list = list()

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

        else:
            for i in find:
                if find[b] is not None:
                    if not flag:
                        name_markets_list.append(Market_Model.objects(location = i).all())
                        print('LOCATION', name_markets_list[b])

                    if name_markets_list[b] is None:
                        name_markets_list.append(Market_Model.objects(name = i).all())
                        print('NAME', name_markets_list[b])
                        break

                    if flag:
                        name_markets_list.append(Market_Model.objects(name=i).all())
                        print('TWO', name_markets_list[b])

                    flag = True
                b += 1

            for j in name_markets_list:
                for k in j:
                    for l in j:
                        print(k['market_id'])
                        if l['market_id'] == k['market_id']:
                            print('SAM!')
                            return_market_list.append(l)


            for market in return_market_list:
                market_list[a] = {
                    "name": market['name'],
                    "location": market['location'],
                    "phone": market['telephone_num']
                }

                a += 1
            print(name_markets_list)
        return market_list, 201
