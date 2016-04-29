#!/usr/bin/env python
#-*-coding:utf-8-*-

import os,sys
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment

reload(sys)
sys.setdefaultencoding("utf-8")
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    from app.models import Role, User

    # 数据库迁移更新
    upgrade()

    # 创建角色
    Role.insert_roles()

    # 自我关注
    User.add_self_follows()

if __name__ == "__main__":
    manager.run()