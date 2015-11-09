from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class SetupForm(Form):

    name = StringField('Blog Name', [
        validators.Required(),
        validators.Length(max=80)
    ])

    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email Address', [validators.DataRequired(),validators.Email()])
    username = StringField('Username', [
        validators.Required(),
        validators.length(min=4,max=25)
    ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.length(min=4,max=80),
        validators.EqualTo('confirm', message='Password do not match')
    ])

    confirm = PasswordField('Repeat Password')
