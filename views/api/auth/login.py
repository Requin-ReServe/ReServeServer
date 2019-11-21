from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token

from models.user.user_model import User_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/user'


@api.resource('/auth')
class Login(Resource):
    def post(self):
        login_id = request.json['id']
        login_pw = request.json['pw']

        finder = User_Model.objects(id=login_id).first()


        if finder is None:
            return abort(409)


        if finder['pw'] == login_pw:
            return {
                "access_token":create_access_token(identity=login_id)
                   }, 200


        return abort(409)