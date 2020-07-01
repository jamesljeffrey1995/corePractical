from flask import render_template, redorect, url_for, request, jsonify
from application import app, pick, db
from random import randint
import requests 
from appication.models import Stance
import sqlalchemy


@app.route('/service2/get_package', methods = ["GET"])
def generate_stance():
    query = Stance.query.filter_by(id=random.randint(1,4))
    stance = query.stance

    stance = { "stance" : stance }

    return jsonify(full_trick)
    
