# coding: UTF-8
from __future__ import absolute_import

from fabtools import require, files, python
from fabtools.python import virtualenv

from fabric.api import env, sudo, cd, settings

env.host_string = 'root@159.203.118.4'

HOTSITE_WORK_PATH = '/root/hotsite/'


def teardown():
    with settings(warn_only=True):
        files.remove(HOTSITE_WORK_PATH, use_sudo=True, recursive=True)


def setup():
    require.git.working_copy('git@github.com:ArthurPBressan/hotsite-sa-bilac-2015.git',
                             path=HOTSITE_WORK_PATH, update=True)
    with cd(HOTSITE_WORK_PATH):
        require.files.directories(['instance', 'tmp'], use_sudo=True)
        require.python.virtualenv(HOTSITE_WORK_PATH)
        with virtualenv(HOTSITE_WORK_PATH):
            python.install('uwsgi')
    deploy()
    with cd(HOTSITE_WORK_PATH), virtualenv(HOTSITE_WORK_PATH):
        sudo('uwsgi --socket :8080 --module="hotsite:create_app()" --touch-reload="/root/uwsgi_file" &')


def deploy():
    require.git.working_copy('git@github.com:ArthurPBressan/hotsite-sa-bilac-2015.git',
                             path=HOTSITE_WORK_PATH, update=True)
    with cd(HOTSITE_WORK_PATH), virtualenv(HOTSITE_WORK_PATH):
        require.python.requirements('requirements.txt')
        require.python.requirements('requirements-db.txt')
        sudo('python manage.py db upgrade')
    reload()


def reload():
    sudo('touch /root/uwsgi_file')
