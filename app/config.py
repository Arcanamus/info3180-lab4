import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    UPLOAD_FOLDER = 'C:\\Users\\Arcan\\Documents\\WebDevLab\\info3180-lab4\\uploads'
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'Password123')