from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user.user_model import User_Model
from models.service.market import Market_Model


api = Api(Blueprint(__name__,__name__))
api.prefix = '/user'


@api.resource('/info')
class UserInformation(Resource):
    @jwt_required
    def get(self):
        user = User_Model.objects(id =
            get_jwt_identity()).first()

        return {
            "name": user['name'],
            "id": user['id'],
            "point": user['point'],
            "phone_num": user['phone_num']
        }, 200

    @jwt_required
    def put(self):
        change_name = request.json['name']
        change_pw = request.json['pw']
        finder = User_Model.objects(id=get_jwt_identity()).first()

        if change_name == None and change_pw == None:
            abort(409)

        elif change_name == None:
            finder.update(
                pw=change_pw
            )

        elif change_pw == None:
            finder.update(
                name=change_name,
            )
        else:
            finder.update(
                name=change_name,
                pw=change_pw
            )

        return '', 201

    @jwt_required
    def delete(self):
        finder = User_Model.objects(id=get_jwt_identity()).first()
        markets = Market_Model.objects(owner_id=get_jwt_identity()).all()

        for market in markets:
            market.delete()

        finder.delete()

        return '', 200