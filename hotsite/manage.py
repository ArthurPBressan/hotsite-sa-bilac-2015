# coding: UTF-8
from __future__ import absolute_import

from flask.ext.script import Manager

manager = Manager(description='Comandos do hotsite')


@manager.command
def criar_admin():
    from hotsite.auth import criar_admin
    criar_admin()
