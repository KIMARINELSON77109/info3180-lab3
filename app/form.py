from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Email
from flask_wtf  import FlaskForm

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

class MyForm(FlaskForm):
    name = StringField('name', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    subject = StringField('subject', validators = [DataRequired()])
    message = TextAreaField('message', validators = [DataRequired()])

    