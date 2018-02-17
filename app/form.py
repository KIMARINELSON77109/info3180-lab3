from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, StringField,SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf  import FlaskForm

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

class MyForm(FlaskForm):
    name = StringField('name', validators = [DataRequired("Name is required!!!!!!!!!")])
    email = StringField('email', validators = [DataRequired("Email is required!!!!!!!!!"), Email("Please Enter vaild email name@example.com")])
    subject = StringField('subject', validators = [DataRequired("Subject for message is required!!!!!!!!!!")])
    message = TextAreaField('message', validators = [DataRequired("Message is required!!!!!!!!")])
    button = SubmitField('send')
    