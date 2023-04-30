import os 
from dotenv import load_dotenv
import app
import MySQL
import flask_migrate

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = flask_migrate
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'username'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'database_name'

    db = MySQL(app)
