from flask import FLask 
from flask_login import LoginManager
import mysql.connector
from .config import Config 
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)

db = mysql.connector.connect(app)

# Flask-login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Instantiate Flask-Migrate library here 
migrate = Migrate(app, db)
from app import views