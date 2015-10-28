# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, redirect, url_for, request, render_template, flash
from flask.ext.wtf import Form
from flask.ext.login import LoginManager, login_user, current_user, logout_user
from wtforms import PasswordField, TextField, validators

from hotsite.models import Aluno
from hotsite.base import db

bp = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, entre com o seu RA e senha do portal'


@login_manager.user_loader
def load_user(user_id):
    user = Aluno.query.filter_by(ra=user_id).first()
    return user


@bp.route("/login/", methods=["GET", "POST"])
def login():
    if not current_user.is_anonymous:
        return redirect(request.args.get('next') or url_for("palestras.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = form.user
        login_user(user)
        return redirect(request.args.get('next') or url_for("palestras.index"))
    elif request.method == 'POST':
        flash(u'Usuário ou senha inválidos.', 'error')
    return render_template("login.html", form=form)


@bp.route("/logout/")
def logout():
    logout_user()
    response = redirect(request.args.get('next') or url_for('palestras.index'))
    return response


def criar_admin():
    user = Aluno(ra='admin', password='admin')
    db.session.add(user)
    db.session.commit()
    return user


class LoginForm(Form):
    username = TextField(u'RA', [validators.Required(message='RA requerido')])
    password = PasswordField(u'Senha', [validators.Required(message='Senha requerida')])

    def __init__(self, **kwargs):
        Form.__init__(self, **kwargs)
        self.user = None

    def validate(self):
        if Form.validate(self):
            username = self.username.data
            password = self.password.data
            self.user = Aluno.check_auth(username, password)
        return self.user is not None


def init_app(app):
    app.register_blueprint(bp, url_prefix='/auth')
    login_manager.init_app(app)
