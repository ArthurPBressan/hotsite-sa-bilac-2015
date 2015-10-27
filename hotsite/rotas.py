# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, render_template, request, redirect, url_for

from hotsite.models import Palestra

bp = Blueprint('palestras', __name__, static_folder='static')


def init_app(app):
    app.register_blueprint(bp, url_prefix='')


@bp.route('/')
def index():
    palestras = {}
    palestras_q = Palestra.query.order_by(Palestra.trilha, Palestra.dia,
                                          Palestra.hora_inicio)
    for palestra in palestras_q:
        palestras_trilha = palestras.setdefault(palestra.trilha, [])
        palestras_trilha.append(palestra)
    trilhas = set(palestra.trilha for palestra in palestras_q)
    return render_template('index.html', palestras=palestras, trilhas=trilhas)


@bp.route('/<palestra>', methods=['GET', 'POST'])
def rate_palestra(palestra):
    palestra = Palestra.query.get_or_404(palestra)
    if request.method == 'POST':
        print request.form
        return redirect(url_for('.index'))
    return render_template('rate_palestra.html', palestra=palestra)
