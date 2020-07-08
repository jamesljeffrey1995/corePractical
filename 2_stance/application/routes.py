from flask import render_template, redirect, url_for, request, jsonify
from application import app
import random
import requests 
import sqlalchemy


@app.route('/service2/get_package', methods = ["GET", "POST"])
def generate_stance():
    stances = {1:"Normal", 2:"Switch", 3:"Nollie", 4:"Fakie"}
    app.logger.info("Database fetched succesful")
    response = stances[random.randint(1,4)]
    stance = { "stance" : response }
    app.logger.info(stance) 
    return jsonify(stance)
