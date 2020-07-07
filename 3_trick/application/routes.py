from flask import render_template, redorect, url_for, request, jsonify
from application import app, pick, db
from random import randint
import requests
from appication.models import Track
import sqlalchemy


@app.route('/service3/get_package', methods = ["GET"])
def generate_trick():
    query = Trick.query.filter_by(id=random.randint(1,Trick.query.order_by(Trick.id.desc()).first()))
    trick = query.trick
    
    trick = { "trick" : trick }

    return jsonify(trick)
