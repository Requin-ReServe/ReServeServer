from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user.user_model import User_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/user'


@api.resource('/point')
class PointManagement(Resource):
    @jwt_required
    def put(self):
        change_point = request.json['point']
        finder = User_Model.objects(id=get_jwt_identity()).first()

        finder.update(
            point = finder['point'] + change_point
        )

        return '', 201