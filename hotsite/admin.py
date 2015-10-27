# coding: UTF-8
from __future__ import absolute_import

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

from hotsite.base import db
from hotsite.models import Aluno, Palestra, PalestraAluno, Role


class _ModelView(ModelView):

    category = None

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', self.name)
        super(_ModelView, self).__init__(self.model, db.session, *args, **kwargs)


class RoleView(_ModelView):
    model = Role
    name = 'Role'


class AlunoView(_ModelView):

    form_excluded_columns = ['palestras']

    model = Aluno
    name = 'Aluno'


class PalestraView(_ModelView):
    form_excluded_columns = ['alunos']

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
        RoleView(),
    ]
    admin = Admin(app)
    for view in views:
        admin.add_view(view)
