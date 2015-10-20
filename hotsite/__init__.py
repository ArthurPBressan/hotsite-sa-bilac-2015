# coding: UTF-8
from __future__ import absolute_import

from flask import Flask
from flask.ext.assets import Environment

from hotsite import base, models, admin


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('settings')
    app.config.from_pyfile('settings_local.py', silent=True)

    if config:
        app.config.update(config)

    Environment(app)
    base.init_app(app)
    models.init_app(app)
    admin.init_app(app)

    @app.route('/')
    def index():
        return "Hello world"

    return app
