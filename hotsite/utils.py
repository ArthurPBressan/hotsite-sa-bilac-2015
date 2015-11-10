# coding: UTF-8
from __future__ import absolute_import

from flask import render_template
from flask.ext.mail import Message

from hotsite.base import mail


def send_mail(template_name, template_kwargs, subject, recipients):
    email_template = render_template('mail/{}'.format(template_name),
                                     **template_kwargs)
    email = Message(subject=subject, recipients=recipients,
                    html=email_template)
    mail.send(email)
    pass
