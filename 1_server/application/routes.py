from application import app
from flask import render_template, redirect, url_for, request
from application.forms import GenerateTrickButton
import requests


@app.route("/", methods = ['GET', "POST"])
@app.route("/home", methods = ['GET', "POST"])
def home():

    form = GenerateTrickButton()
    if request.method == "GET":
        full_trick = {"stance" : "",
                "trick" : "",
                "steeze": ""}
        return render_template("home.html", title = "Home", form = form)

    if form.validate_on_submit():
        app.logger.info(f"Package requested")
        response = requests.get("http://4_SKATE:5003/service4/get_package")
        full_trick = response.json()
        app.logger.info(f"{full_trick}")
    return render_template("home.html", title = "Home", form = form, full_trick = full_trick)
    
