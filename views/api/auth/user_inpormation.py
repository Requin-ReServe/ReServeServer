from flask import Blueprint, request, abort
from flask_restful import Api, Resource

from models.user.user_model import User_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/auth'


@api.resource('/user-inpormation')
class UserInformation(Resource):
    def get(self):
        user = User_Model.objects(id ='migskiang').first()

        return {
            "name": user['name'],
            "id": user['id'],
            "point": user['point'],
            "user_type": user['user_type']
        }, 200


    def post(self):
        change_name = request.json['name']
        change_pw = request.json['pw']
        finder = User_Model.objects(id= 'migskiang').first()

        finder.update(
            name=change_name,
            pw = change_pw
        )


        return '', 201

