#coding=UTF-8
from __future__ import absolute_import

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand

from hotsite import create_app
from hotsite.manage import manager as hotsite_manager

app = create_app()

manager = Manager(app)
manager.add_command('hotsite', hotsite_manager)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())


if __name__ == '__main__':
    manager.run()
