import os 

POSTGRESQL_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
POSTGRESQL_TRACK_MODIFICATIONS = False