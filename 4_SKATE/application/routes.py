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
        app.logger.info("{stance} {trick}")
        steeze = {"steeze": ""}
        if stance["stance"] == "Nollie":
                steeze["steeze"] = 40
        elif stance["stance"] == "Switch":
                steeze["steeze"] = 30
        elif stance["stance"] == "Fakie":
                steeze["steeze"] = 20
        elif stance["stance"] == "Normal":
                steeze["steeze"] = 10
        num = steeze["steeze"]
        if trick["trick"] == "Kickflip":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 5
        elif trick["trick"] == "Heelflip":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 10
        elif trick["trick"] == "Treflip":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 15
        elif trick["trick"] == "Lazerflip":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 20
        elif trick["trick"] == "Hardflip":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 25
        elif trick["trick"] == "Inward Heelflip":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 30
        elif trick["trick"] == "Hospital Flip":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 35
        elif trick["trick"] == "Pop-shuvit":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 40
        elif trick["trick"] == "Impossible":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 45
        elif trick["trick"] == "FS Pop-Shuvit":
                Num = steeze["steeze"]
                steeze["steeze"] = num + 50
        stance.update(trick)
        stance.update(steeze)
        return jsonify(stance)
