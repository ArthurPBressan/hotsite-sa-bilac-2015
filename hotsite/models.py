# coding: UTF-8
from __future__ import absolute_import

from flask.ext.login import make_secure_token, UserMixin

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, Date, Text, Time

from hotsite.base import db


def init_app(app):
    pass


class Aluno(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    ra = Column(String(255))
    nome = Column(String(255))
    password = Column(String(255))
    palestras = relationship('PalestraAluno', backref='aluno')

    @db.validates('password')
    def tokenize_password(self, key, value):
        return make_secure_token(value)

    @classmethod
    def check_auth(cls, ra, password):
        if not password:
            return None
        password = make_secure_token(password)
        return cls.query.filter_by(ra=ra, password=password).first()

    def get_id(self):
        return self.ra

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def __repr__(self):
        return '{}-{}'.format(self.nome, self.ra)


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

    alunos = relationship('PalestraAluno', backref='palestra')


class PalestraAluno(db.Model):
    id = Column(Integer, primary_key=True)

    palestra_id = Column(Integer, ForeignKey('palestra.id'))
    aluno_id = Column(Integer, ForeignKey('aluno.id'))

    rating = Column(Integer)
    comentario = Column(Text)
