from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    username = StringField('Username: ', [
        validators.length(
            min=4, max=50, message='El username se encuentra fuera de rango'),
        validators.Required()])
    password = PasswordField('Password: ', [
        validators.Required()
    ])
