#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, FileField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask.ext.pagedown.fields import PageDownField

from ..models import Role, User

class NameForm(Form):
    name = StringField('名字 ', validators=[Required()])
    submit = SubmitField('提交')

class EditProfileForm(Form):
    location = StringField('所在地', validators=[Length(0, 64)])
    about_me = TextAreaField('个性签名')
    submit = SubmitField('提交')

class EditProfileAdminForm(Form):
    email = StringField('邮件地址', validators=[Required(), Length(1, 64),
                                             Email()])
    confirmed = BooleanField('确认')
    name = StringField('名字', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          '名字由字母组成, '
                                          '数字、小数点')])
    role = SelectField('角色', coerce=int)
    location = StringField('所在地', validators=[Length(0, 64)])
    about_me = TextAreaField('个性签名')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱地址已经注册')

    def validate_name(self, field):
        if field.data != self.user.name and \
                User.query.filter_by(name=field.data).first():
            raise ValidationError('名字已经被使用')

class PostForm(Form):
    body = PageDownField('写点什么', validators=[Required()])
    submit = SubmitField('提交')

class CommentForm(Form):
    body = StringField('说点什么', validators=[Required()])
    submit = SubmitField('提交')

class UploadAvatarForm(Form):
    uploadfile = FileField("上传头像",validators=[Required()])
    submit = SubmitField("确定")

class UploadPicForm(Form):
    uploadfile = FileField("上传图片",validators=[Required()])
    picname = StringField("图片名", validators=[Required()])
    submit = SubmitField("确定")