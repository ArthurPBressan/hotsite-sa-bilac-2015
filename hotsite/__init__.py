# coding: UTF-8
from __future__ import absolute_import

import locale
locale.setlocale(locale.LC_ALL, ('pt_BR', 'UTF-8'))

from flask import Flask
from flask.ext.assets import Environment
from raven.contrib.flask import Sentry

from hotsite import base, models, admin, rotas, auth


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('settings')
    app.config.from_pyfile('settings_local.py', silent=True)

    if config:
        app.config.update(config)

    Environment(app)
    Sentry(app)

    base.init_app(app)
    auth.init_app(app)
    models.init_app(app)
    admin.init_app(app)
    rotas.init_app(app)

    return app
