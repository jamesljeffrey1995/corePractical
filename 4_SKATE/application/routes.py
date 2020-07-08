from flask import render_template, redirect, url_for, request, jsonify
from application import app
from random import randint
import requests
import sqlalchemy


@app.route('/service4/get_package', methods = ["GET", "POST"])
def generate_full_trick():
    app.logger.info("Request Recieved")    

    service2_response = requests.get("http://2_stance:5001/service2/get_package")
    app.logger.info("service 2 Request Recieved")
    service3_response = requests.get("http://3_trick:5002/service3/get_package")
    app.logger.info("service 3 Request Recieved")
    stance = service2_response.json()
    trick = service3_response.json()

    stance.update(trick)
    app.logger.info(f"Object being sent from service 4: {stance}")  
    return jsonify(stance)
