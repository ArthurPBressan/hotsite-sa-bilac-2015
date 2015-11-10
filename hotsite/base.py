# coding: UTF-8
from __future__ import absolute_import

from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.assets import Environment
from raven.contrib.flask import Sentry

db = SQLAlchemy()
mail = Mail()


def init_app(app):
    db.init_app(app)
    mail.init_app(app)
    Environment(app)
    Sentry(app)
    Migrate(app, db)
