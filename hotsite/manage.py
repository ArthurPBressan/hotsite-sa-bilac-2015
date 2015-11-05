# coding: UTF-8
from __future__ import absolute_import

from flask.ext.script import Manager

manager = Manager(description='Comandos do hotsite')


@manager.command
def criar_admin():
    from hotsite.auth import criar_admin
    criar_admin()


@manager.command
def importar_usuarios(filename):
    from hotsite.base import db
    from hotsite.models import Aluno
    from unicodecsv import DictReader
    with open(filename, 'rb') as csvfile:
        csvreader = DictReader(csvfile)
        for row in csvreader:
            nome, ra, password = row['Nome'], row['RA'], row['CPF']
            print nome, ra, password
            aluno = Aluno(nome=nome, ra=ra, password=password)
            db.session.add(aluno)
    db.session.commit()
