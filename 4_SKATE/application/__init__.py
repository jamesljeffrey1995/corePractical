from flask import Flask
from os import getenv


app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')

from application import routes
~                                      
