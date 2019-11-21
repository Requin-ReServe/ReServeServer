from flask import Blueprint, request, abort
from flask_restful import Api, Resource

from models.user.user_model import User_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/user'


@api.resource('/register')
class Register(Resource):
    def post(self):
        register_id = request.json['id']
        register_name = request.json['name']
        register_pw = request.json['pw']
        register_phone_num = request.json['phone_num']
        user_type = request.json['type']
        basic_point = 0


        finder = User_Model.objects(id=register_id).first()


        if finder is not None:
            abort(409)


        User_Model(
            id = register_id,
            pw = register_pw,
            name = register_name,
            point = basic_point,
            phone_num = register_phone_num,
            user_type = user_type
        ).save()

        return '', 201