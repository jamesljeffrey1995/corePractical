from application import app
import unittest
from flask import url_for, jsonify
from flask_testing import TestCase
import requests
import requests_mock
from os import getenv
class TestBase(TestCase):
    def create_app(self):

 
 

 
# pass in configurations for test database

 
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
        SECRET_KEY=getenv('MY_SECRET_KEY'),
        WTF_CSRF_ENABLED=False,
        DEBUG=True
        )
        return app

class TestResponse(TestBase):
    def test_app(self):
        trick = {"stance":"Normal", "trick":"Kickflip"}
       # response = self.client.post('http://0.0.0.0:5003/service4/get_package', data={"stance":"Normal", "trick":"Kickflip"})
       # self.assertIn(trick["stance"], response.data)
        with requests_mock.mock() as x:
            x.get("http://2_stance:5001/service2/get_package", json={"stance":"Normal"})
            x.get("http://3_trick:5002/service3/get_package", json={"trick":"Kickflip"})
            response = self.client.post(url_for('generate_full_trick'))
            app.logger.info(response.data)
            self.assertIn(b"stance", response.data)
            self.assertIn(b"trick", response.data)
