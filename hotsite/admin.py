# coding: UTF-8
from __future__ import absolute_import

from flask import current_app
from flask.ext.admin import Admin
from flask.ext.admin import BaseView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

from hotsite.base import db
from hotsite.models import Aluno, Palestra, PalestraAluno


def handle_view(self, name, **kwargs):
    if not current_user.is_authenticated or current_user.ra != 'admin':
        return current_app.login_manager.unauthorized()

BaseView._handle_view = handle_view


class _ModelView(ModelView):

    category = None

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', self.name)
        super(_ModelView, self).__init__(self.model, db.session, *args, **kwargs)


class AlunoView(_ModelView):

    form_excluded_columns = ['palestras', 'password']
    column_filters = ['ra', 'nome']

    model = Aluno
    name = 'Aluno'


class PalestraView(_ModelView):
    form_excluded_columns = ['alunos', 'titulo_slug']

    model = Palestra
    name = 'Palestra'


class PalestraAlunoView(_ModelView):
    model = PalestraAluno
    name = 'Palestra x Aluno'


def init_app(app):
    views = [
        AlunoView(),
        PalestraView(),
        PalestraAlunoView(),
    ]
    admin = Admin(app)
    for view in views:
        admin.add_view(view)
