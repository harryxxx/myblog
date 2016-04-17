from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User

class NameForm(Form):
    name = StringField('name: ', validators=[Required()])
    submit = SubmitField('Submit')

class EditProfileForm(Form):
    location = StringField('Location', validators=[Length(0, 64)])
    avatar = StringField('Avatar', validators=[Length(0, 128)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

class EditProfileAdminForm(Form):
    avatar = StringField('Avatar', validators=[Length(0, 128)])
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    confirmed = BooleanField('Confirmed')
    name = StringField('Name', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Names must have only letters, '
                                          'numbers, dots or underscores')])
    role = SelectField('Role', coerce=int)
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_name(self, field):
        if field.data != self.user.name and \
                User.query.filter_by(name=field.data).first():
            raise ValidationError('Name already in use.')