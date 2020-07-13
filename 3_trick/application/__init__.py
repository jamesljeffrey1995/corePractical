from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
user = getenv('USERNAME')
password = getenv('PASSWORD')
ip = getenv('IP')
database = getenv('DATABASE')
user="root"
password="890111e5"
ip="34.89.16.196"
database="tricks"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + user + ':' + password + '@' + ip + '/' + database
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')

from application import routes
