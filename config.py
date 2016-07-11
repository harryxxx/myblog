#!/usr/bin/env python
#-*-coding:utf-8-*-

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Harry]'
    FLASKY_MAIL_SENDER = 'harryx520@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME=0.5
    UPLOAD_FOLDER = "uploads"
    UPLOAD_PIC_FOLDER = "uploadpics"
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024 # max upload size < 3M
    ALLOWED_EXTENSIONS = set(['jpg','png','JPG','PNG'])

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql://flask:admin@localhost/flaskdb'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI ='mysql://flask:admin@localhost/flaskdb'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI ='mysql://flask:admin@localhost/flaskdb'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': ProductionConfig
}

