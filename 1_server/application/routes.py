from application import app
from flask import render_template, redirect, url_for, request
from application.forms import GenerateTrickButton
import requests


@app.route("/")
@app.route("/home")
def home():

    generate_trick = GenerateTrickButton()

    if request.method == "GET":
        full_trick = {
                "stance" : "",
                "trick" : ""
                }

        if generate_trick.is_submitted():
            response = requests.get("http://SKATE:5000/service4/get_package")
            full_trick = response.json()
