from application.models import Stance
from flask import render_template, redirect, url_for, request, jsonify
from application import app, db
import random
import requests
import sqlalchemy


@app.route('/service2/get_package', methods = ["GET", "POST"])
def generate_stance():
    app.logger.info("Recieved")
    randomnum = random.randint(1,4)
    query = Stance.query.filter_by(id=randomnum).first()
    app.logger.info(query.stance)
    stance = query.stance
    stance = { "stance" : stance }
    return jsonify(stance)
