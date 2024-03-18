from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp



class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Regexp(regex=r'^(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d]+$',
                                                       message="Password must contain only letters and digits"), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


class EnterIdForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
