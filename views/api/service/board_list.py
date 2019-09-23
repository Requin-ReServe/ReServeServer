from flask import Blueprint, request, abort
from flask_restful import Api, Resource

from models.service.board_list import Boardlist_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/service'


@api.resource('/board-list')
class boardList(Resource):
    def get(self):
        board_id = request.json['board_id']

        return {
             #MONGO BOARD DATA
        }

    def post(self):
        auth_id = request.json['auth_id']
        menu = request.json['menu']

        board_id = None


        return '', 201