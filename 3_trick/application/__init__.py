from flask import Flask
from os import getenv


app.config['SQLALCHEMY_DATABASE_URI']=getenv('SURF_URI')
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')

from application import routes
~                                      
