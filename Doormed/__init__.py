from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail, Message
from flask_admin import Admin
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doormed.db'
app.config['SECRET_KEY']="team_doormed"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['MAIL_SUBJECT_PREFIX'] =  '[New Query]'
app.config['MAIL_SENDER'] = 'ADMIN <amitnitt015@gmail.com>'
app.config['ADMIN'] = os.environ.get('ADMIN') 

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

admin = Admin(app)

migrate = Migrate(app,db)
login_manager = LoginManager(app)
login_manager.login_view = 'user_login'
login_manager.login_message_category = 'danger'

login_seller = LoginManager(app)
login_seller.login_view = 'seller_user'
login_seller.login_message_category = 'danger'

from . import routes
from Doormed.main import routes
from Doormed.seller import routes
from Doormed.customer import routes
from Doormed.contact import routes
from Doormed.errors import handlers

from Doormed.cart import routes
