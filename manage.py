#!flask/bin/python

from flask.ext.script import Manager, Command,Option
from app import app

manager=Manager(app)

if __name__ == '__main__':
	manager.run()
