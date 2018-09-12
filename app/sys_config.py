import os

class Config():
	
	# System configuration
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	# Database configuration
	DATABASE_HOST = 'localhost'
	DATABASE_USERNAME = 'sandip'
	DATABASE_PASSWORD = 'sandip08'
	DATABASE_NAME = 'recruitement_db'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+':3306/'+ DATABASE_NAME
	# '{db}+{db_api}://{db_user}:{pwd}@{server}:{port}/{db_name}'
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	# # System email configuration
	# SYSTEM_EMAIL = ''
	# EMAIL_USERNAME = ''
	# EMAIL_PASSWORD = ''
	# SMTP_SERVER_NAME = 'outlook-emeawest.office365.com'
	# SMTP_PORT = 587