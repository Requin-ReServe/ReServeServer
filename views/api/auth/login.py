from flask import Blueprint, request
from flask_restful import Api, Resource

from models.user.user_model import User_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/auth'


@api.resource('/login')
class Login(Resource):
    def post(self):
        login_id = request.json['id']
        login_pw = request.json['pw']

        finder = User_Model.objects(id=login_id).first()


        if finder is None:
            return '', 405


        if finder['pw'] == login_pw:
            return '', 200


        return '', 405