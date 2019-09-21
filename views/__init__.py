from flask import Flask
from mongoengine import connect

from const import _MONGO_SETTING


def create_app(*config_cls):
    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    Route(app_)
    connect(**_MONGO_SETTING)

    return app_


def Route(app : Flask):
    from views.api.auth import test_api, register, login
    app.register_blueprint(test_api.api.blueprint)
    app.register_blueprint(register.api.blueprint)
    app.register_blueprint(login.api.blueprint)