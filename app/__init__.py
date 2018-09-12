#!/usr/bin/python
# System import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import logging, os
from logging.handlers import SMTPHandler, RotatingFileHandler

#=========================================================================================================================#
#=========================================================================================================================#

# Local import 
from app.sys_config import Config

#=========================================================================================================================#
#=========================================================================================================================#

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
from app import views, models, errors

#=========================================================================================================================#
#============================================================ End ========================================================#

if  app.debug:
    if not os.path.exists('logs'):os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/recruit.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Recruitment log startup')
	# app.logger.info('{0} {1} {2}'.format(req.method, req.relative_uri, resp.status))




#=========================================================================================================================#
