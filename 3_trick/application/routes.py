from flask import render_template, redirect, url_for, request, jsonify
from application import app, db
import random
import requests
from application.models import Tricks
import sqlalchemy


@app.route('/service3/get_package', methods = ["GET", "POST"])
def generate_trick():
    app.logger.info("Recieved")
    randomnum = random.randint(1,10)
    query = Tricks.query.filter_by(id=randomnum).first()
    app.logger.info(query.trick)
    trick = query.trick
    
    trick = { "trick" : trick }

    return jsonify(trick)
