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
    from views.api.auth import register, login, user_information, charge_point
    app.register_blueprint(register.api.blueprint)
    app.register_blueprint(login.api.blueprint)
    app.register_blueprint(user_information.api.blueprint)
    app.register_blueprint(charge_point.api.blueprint)

    from views.api.service import (
        register_market, market_list, show_market, my_market, reservation,
        reservation_detail, owner_show_reservation_list, payment )
    app.register_blueprint(register_market.api.blueprint)
    app.register_blueprint(market_list.api.blueprint)
    app.register_blueprint(show_market.api.blueprint)
    app.register_blueprint(my_market.api.blueprint)
    app.register_blueprint(reservation.api.blueprint)
    app.register_blueprint(reservation_detail.api.blueprint)
    app.register_blueprint(owner_show_reservation_list.api.blueprint)
    app.register_blueprint(payment.api.blueprint)

    from views.api.util import band_check_band_check
    app.register_blueprint(band_check_band_check.api.blueprint)