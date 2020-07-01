from flask import render_template, redorect, url_for, request, jsonify
from application import app, pick, db
from random import randint
import requests
from appication.models import Stance
import sqlalchemy


@app.route('/service4/get_package', methods = ["GET"])
def generate_full_trick():
    

    service2_response = requests.get("http://stance_generator:5000/service2/get_package")
    service3_response = requests.get("http://trick_generator:5000/service3/get_package")
    stance = service2_response.json()
    trick = service3_response.json()
    return jsonify(full_trick)
