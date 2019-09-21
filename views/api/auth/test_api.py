from flask import Blueprint, request
from flask_restful import Api, Resource


api = Api(Blueprint(__name__,__name__))

@api.resource('/')
class test(Resource):
    def get(self):
        return {
            'METHOD':'GET'
        }, 201


    def post(self):
        try:
            data = request.json['data']
            print(data)
        except:
            return {
                'METHOD': 'NULL'
            }, 400

        return {
            'METHOD':data+"바보"
        }, 201