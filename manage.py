#!/usr/bin/env python
#-*-coding:utf-8-*-

import os,sys
from flask.ext.script import Manager

from app import create_app

reload(sys)
sys.setdefaultencoding("utf-8")
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

if __name__ == "__main__":
    manager.run()