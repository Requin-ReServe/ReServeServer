from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user.user_model import User_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/auth'


@api.resource('/user-information')
class UserInformation(Resource):
    @jwt_required
    def get(self):
        user = User_Model.objects(id =
            get_jwt_identity()).first()

        return {
            "name": user['name'],
            "id": user['id'],
            "point": user['point'],
            "user_type": user['user_type']
        }, 200

    @jwt_required
    def post(self):
        change_name = request.json['name']
        change_pw = request.json['pw']
        finder = User_Model.objects(id=get_jwt_identity()).first()

        finder.update(
            name=change_name,
            pw = change_pw
        )


        return '', 201

