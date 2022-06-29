import unittest

from app import create_app
from app.extensions import db
from flask import current_app


class BasicTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)
