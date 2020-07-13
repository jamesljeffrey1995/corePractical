from application import app
import unittest
from flask import url_for, jsonify
from flask_testing import TestCase
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_app(self):
        response = self.client.get('/service2/get_package').get_json()['stance']
        assert response == "Fakie" or response == "Switch" or response == "Nollie" or response == "Normal"
