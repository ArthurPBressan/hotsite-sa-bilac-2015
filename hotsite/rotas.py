# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, render_template
from ordered_set import OrderedSet

from hotsite.base import db
from hotsite.models import Palestra

bp = Blueprint('palestras', __name__)


def init_app(app):
    app.register_blueprint(bp, url_prefix='')


@bp.route('/')
def index():
    partial_palestras_q = \
        db.session.query(Palestra.trilha, Palestra.hora_inicio, Palestra.dia) \
        .order_by(Palestra.trilha, Palestra.dia, Palestra.hora_inicio)

    trilhas = OrderedSet(palestra.trilha for palestra in partial_palestras_q)
    dias = OrderedSet(palestra.dia for palestra in partial_palestras_q)
    horarios = OrderedSet(palestra.hora_inicio for palestra in partial_palestras_q)

    palestras = {}
    for palestra in Palestra.query.all():
        _trilha_map = palestras.setdefault(palestra.trilha, {})
        _dia_map = _trilha_map.setdefault(palestra.dia, {})
        _dia_map.setdefault(palestra.hora_inicio, palestra)
    return render_template('index.html', trilhas=trilhas, dias=dias,
                           horarios=horarios, palestras=palestras)
