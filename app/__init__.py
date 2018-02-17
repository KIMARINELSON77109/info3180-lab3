from flask import Flask
from flask_mail import Mail


app = Flask(__name__)

app.config['SECRET_KEY'] = 'HIDDEN'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'a0054a93ef5bd1'
app.config['MAIL_PASSWORD'] = '36b4a846be8441'

mail = Mail(app)

from app import views