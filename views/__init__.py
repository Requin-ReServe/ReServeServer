from flask import Flask
from mongoengine import connect
from flask_jwt_extended import JWTManager

from const import _MONGO_SETTING


def create_app(*config_cls):
    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    JWTManager().init_app(app_)
    Route(app_)
    connect(**_MONGO_SETTING)

    return app_


def Route(app : Flask):
    from views.api.auth import test_api, register, login, user_impormation
    app.register_blueprint(test_api.api.blueprint)
    app.register_blueprint(register.api.blueprint)
    app.register_blueprint(login.api.blueprint)
    app.register_blueprint(user_impormation.api.blueprint)

    from views.api.service import register_market, board_list, order_list, market_list
    app.register_blueprint(register_market.api.blueprint)
    app.register_blueprint(board_list.api.blueprint)
    app.register_blueprint(market_list.api.blueprint)