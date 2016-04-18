#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from ..models import User

class LoginForm(Form):
    email = StringField('邮件地址', validators=[Required(), Length(1, 64),Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

class RegistrationForm(Form):
    email = StringField('邮件地址', validators=[Required(), Length(1, 64),
                                           Email()])
    name = StringField('名字', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          '名字只能有单词, '
                                          '数字、小数点')])
    password = PasswordField('密码', validators=[
        Required(), EqualTo('password2', message='密码不匹配.')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮件已经注册过了.')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('名字已经被使用了.')

class ChangePasswordForm(Form):
    old_password = PasswordField('旧密码', validators=[Required()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='密码不匹配')])
    password2 = PasswordField('确认新密码', validators=[Required()])
    submit = SubmitField('更新密码')

class PasswordResetRequestForm(Form):
    email = StringField('邮件地址', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('重置密码')


class PasswordResetForm(Form):
    email = StringField('邮件地址', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='密码必须匹配')])
    password2 = PasswordField('确认新密码', validators=[Required()])
    submit = SubmitField('重置密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮件地址错误.')

class ChangeEmailForm(Form):
    email = StringField('新邮件地址', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('地址', validators=[Required()])
    submit = SubmitField('更新邮件地址')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮件地址已经注册过了.')