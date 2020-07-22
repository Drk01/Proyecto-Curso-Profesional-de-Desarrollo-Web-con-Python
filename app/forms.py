from wtforms import Form, StringField, PasswordField, validators, BooleanField
from wtforms.fields.html5 import EmailField
import email_validator


class LoginForm(Form):
    username = StringField('Username: ', [
        validators.length(
            min=4, max=50, message='El username se encuentra fuera de rango'),
        validators.Required()])
    password = PasswordField('Password: ', [
        validators.Required(message='La contraseña es requerida')
    ])


class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50)
    ])
    email = EmailField('Correo electrónico', [
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email válido')
    ])
    password = PasswordField('Password', [
        validators.Required(message='El password es requerido'),
        validators.EqualTo('confirm_password',
                           message='La contraseña no coíncide')
    ])
    confirm_password = PasswordField('Confirmar contraseña')
    accept = BooleanField('', [
        validators.DataRequired()
    ])
