from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_login import login_manager
import os

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app,db)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doormed.db'
app.config['SECRET_KEY']="team_doormed"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_SUBJECT_PREFIX'] = '[QUERY]'
app.config['FLASK_MAIL_SENDER'] = 'ADMIN <user@gmail.com>'
app.config['ADMIN'] = os.environ.get('ADMIN')

mail = Mail(app)

login_manager = login_manager.LoginManager(app)
login_manager.login_view = 'user_login'
login_manager.login_message_category = 'danger'

from Doormed.main import routes
from Doormed.seller import routes
from Doormed.customer import routes
from Doormed.contact import routes
# from Doormed.cart import routes
