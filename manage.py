# encoding: utf-8
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bpython
import flask
from flask.ext.script import Manager
import pdb;pdb.set_trace()
from luanblog import app
from luanblog import models
from luanblog.auth import create_user as auth_create_user

manager = Manager(app)

@manager.command
def shell():
    context = dict(app=app, models=models)
    args = "-i".split()
    banner = u"Utilização do Bpython como shell, com integração no flask."

    bpython.embed(locals_=context, args=args, banner=banner)


@manager.option('-u', '--username', dest='username', default='admin', 
                help='Your username, default is "admin"')
@manager.option('-p', '--password', dest='password', default='1q2w3e', 
                help='Your password, default is "1q2w3e"')
def create_user(username, password):
    created = auth_create_user(username, password)
    print(created)

if __name__ == "__main__":
    manager.run()
