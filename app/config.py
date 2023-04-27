import os 
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = flask_migrate
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    