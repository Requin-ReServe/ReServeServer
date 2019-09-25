import random

from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from models.service.board_list import Boardlist_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'

@api.resource('/board-list')
class boardList(Resource):
    def get(self):
        board_id = request.json['board_id']

        board = Boardlist_Model.objects(board_id = board_id).first()

        board_list = {}
        a = 0

        for menu in board['menu']:
            board_list[a] = {
                menu['name'] : menu['price']
            }
            a += 1

        return {
            "menu":board_list
        }, 200

    @jwt_required
    def post(self):
        board_id = request.json['board_id']
        market_id = request.json['market_id']
        menu = request.json['menu']

        finder = Boardlist_Model.objects(board_id=board_id).first()

        if finder is None:
            while True:
                create_board_id = random.randrange(11111,99999)

                if Boardlist_Model.objects(board_id = create_board_id).first() is None:
                    break

            Boardlist_Model(
                board_id = create_board_id,
                market_id = market_id,
                menu = menu
            ).save()

            # Save Request Example
            # {
            #     "board_id": "57192",
            #     "auth_id": "12345",
            #     "menu": [{
            #         "name": "mgiskingasdf",
            #         "price": "50042"
            #     }]
            # }

        else:
            finder.menu.append(menu)
            finder.save()

            # Update Request Example
            # {
            #     "board_id": "57192",
            #     "auth_id": "12345",
            #     "menu": {
            #         "name": "mgiskingasdf",
            #         "price": "50042"
            #     }
            # }

        return '', 201