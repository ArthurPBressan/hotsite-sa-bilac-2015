# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, render_template, request, redirect, url_for, \
    current_app
from flask.ext.login import login_required, current_user

from hotsite.models import Palestra, PalestraAluno
from hotsite.base import db
from hotsite.utils import send_mail

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


@bp.route('/favicon.ico')
def favicon():
    return redirect(url_for('.static', filename='img/favicon.ico'))


@bp.route('/login/')
def login():
    return redirect(url_for('auth.login'))


@bp.route('/palestras/<palestra>', methods=['GET', 'POST'])
@login_required
def rate_palestra(palestra):
    palestra = Palestra.query.get_or_404(palestra)
    palestra_aluno = PalestraAluno.query \
        .filter_by(palestra_id=palestra.id, aluno_id=current_user.id) \
        .first()
    if request.method == 'POST' and not palestra_aluno:
        comentario = request.form['comentario']
        rating = int(request.form['rating'])
        palestra_aluno = PalestraAluno(palestra_id=palestra.id, rating=rating,
                                       comentario=comentario,
                                       aluno_id=current_user.id)
        db.session.add(palestra_aluno)
        db.session.commit()
        recipients = current_app.config.get('MAIL_DEFAULT_RATE_RECIPIENTS')
        send_mail('rate.html', {'palestra_aluno': palestra_aluno},
                  u'Nova avaliação de palestra', recipients)
    return render_template('rate_palestra.html', palestra=palestra,
                           palestra_aluno=palestra_aluno)
