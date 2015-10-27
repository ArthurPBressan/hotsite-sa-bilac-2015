# coding: UTF-8
from __future__ import absolute_import

from flask.ext.security import SQLAlchemyUserDatastore, UserMixin, RoleMixin

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Integer, String, Date, Text, Time, Boolean

from hotsite.base import db, security


def init_app(app):
    user_datastore = SQLAlchemyUserDatastore(db, Aluno, Role)
    security.init_app(app, user_datastore)


roles_alunos = db.Table(
    'roles_alunos',
    Column('aluno_id', Integer(), ForeignKey('aluno.id')),
    Column('role_id', Integer(), ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

    def __repr__(self):
        return self.name


class Aluno(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    ra = Column(String(255))
    nome = Column(String(255))
    password = Column(String(255))
    roles = relationship('Role', secondary=roles_alunos,
                         backref=backref('alunos', lazy='dynamic'))
    active = Column(Boolean(), default=True)

    palestras = relationship('PalestraAluno', backref='aluno')

    def __repr__(self):
        return '{} ({})'.format(self.email, ', '.join([role.name for role in self.roles]))


class Palestra(db.Model):
    id = Column(Integer, primary_key=True)

    trilha = Column(String(255))
    titulo = Column(String(255))
    resumo = Column(Text)
    bio_autor = Column(Text)
    autor = Column(String(255))

    dia = Column(Date)
    hora_inicio = Column(Time)
    hora_fim = Column(Time)

    alunos = relationship('PalestraAluno', backref='palestras')


class PalestraAluno(db.Model):
    id = Column(Integer, primary_key=True)

    palestra_id = Column(Integer, ForeignKey('palestra.id'))
    aluno_id = Column(Integer, ForeignKey('aluno.id'))

    rating = Column(Integer)
    comentario = Column(Text)
