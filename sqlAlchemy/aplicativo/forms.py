from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from aplicativo.models import User,Post

class RegistrationForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired()])
    email= StringField('email',validators=[DataRequired(), Email()])
    password=PasswordField ('password',validators=[DataRequired()])
    confirm_password=PasswordField ('confirm password',validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign up')
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError (f'thats username already exist, pls choose another one')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError (f'thats email already exist, pls choose another one')


class LoginForm (FlaskForm):
    username= StringField('Username: ',validators=[DataRequired()])
    password=PasswordField ('password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Log in')