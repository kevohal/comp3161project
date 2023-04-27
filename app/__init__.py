from flask import Flask 
from flask_login import LoginManager
from flask_mysqldb import MySQL
from .config import Config 
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)

db = MySQL(app)

# Flask-login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Instantiate Flask-Migrate library here 
migrate = Migrate(app, db)
from app import views