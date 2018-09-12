#!flask/bin/python
from app import app, db
if __name__ == '__main__':
	db.create_all()
	app.secret_key = 'you will never guess'
	app.debug = True
	app.run()