from application import db
from application.models import Tricks

db.drop_all()
db.create_all()
