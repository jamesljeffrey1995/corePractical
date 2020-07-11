from application import app
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRoutes(TestBase):
    print("hello")
