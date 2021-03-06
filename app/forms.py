from wtforms import Form, StringField, PasswordField, validators, BooleanField
from wtforms.fields.html5 import EmailField
import email_validator
from werkzeug.security import generate_password_hash
from .models import User


def cody_validator(form, field):
    if field.data == "Cody" or field.data == "cody":
        raise validators.ValidationError("El username no es permitido")


class LoginForm(Form):
    username = StringField(
        "Username: ",
        [
            validators.length(
                min=4, max=50, message="El username se encuentra fuera de rango"
            ),
            validators.Required(),
        ],
    )
    encrypted_password = PasswordField(
        "Password: ", [validators.Required(
            message="La contraseña es requerida")]
    )

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.encrypted_password = generate_password_hash(value)


class RegisterForm(Form):
    username = StringField("Username", [validators.length(min=4, max=50)])
    email = EmailField(
        "Correo electrónico",
        [
            validators.length(min=6, max=100),
            validators.Required(message="El email es requerido"),
            validators.Email(message="Ingrese un email válido"),
        ],
        email_validator,
    )
    password = PasswordField(
        "Password",
        [
            validators.Required(message="El password es requerido"),
            validators.EqualTo("confirm_password",
                               message="La contraseña no coíncide"),
        ],
    )
    confirm_password = PasswordField("Confirmar contraseña")
    accept = BooleanField("", [validators.DataRequired()])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError(
                "El username ya se encuentra en uso")

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError("El email ya se encuentra en uso")

    def validate(self):
        if not Form.validate(self):
            return False

        if len(self.password) < 3:
            self.password.errors.append('El password es demasiado corto')
            return False

        return True
