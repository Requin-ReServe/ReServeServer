from flask import Flask


def create_app(*config_cls):
    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    Route(app_)

    return app_


def Route(app : Flask):
    pass