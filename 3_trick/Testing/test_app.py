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
        response = self.client.get('/service3/get_package', json={"trick":"Kickflip"})
        assert response.status_code == 200
