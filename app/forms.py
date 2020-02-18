from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Email, EqualTo, DataRequired

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField()
    submit = SubmitField('Login')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Submit')

class ReminderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    amount = StringField('Amount', validators=[DataRequired()])
    due_on = StringField('Due Date', validators=[DataRequired()])
    remind_on = StringField('Reminder Date', validators=[DataRequired()])
    repeat = BooleanField()
    enabled = BooleanField()
    submit = SubmitField('Create Reminder')

class UpdateReminderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    amount = StringField('Amount', validators=[DataRequired()])
    due_on = StringField('Due Date', validators=[DataRequired()])
    remind_on = StringField('Reminder Date', validators=[DataRequired()])
    repeat = BooleanField()
    enabled = BooleanField()
    submit = SubmitField('Create Reminder')