import unittest

from app import create_app
from app.extensions import db

from app.models.user import User, UserData


class UserModelTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('test')
        self.app_context = self.app.app_context()

        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(UserData('username', 'password', 'example@email.com', True))

        self.assertTrue(u.hash is not None)

    def test_no_password_getter(self):
        u = User(UserData('username', 'password', 'example@email.com', True))

        with self.assertRaises(AttributeError):
            u.password()

    def test_password_verification(self):
        u = User(UserData('username', 'password', 'example@email.com', True))

        self.assertTrue(u.verify_password('password'))
        self.assertFalse(u.verify_password('notpassword'))

    def test_password_salts_are_random(self):
        u = User(UserData('username', 'password', 'example@email.com', True))
        u2 = User(UserData('username', 'password', 'example@email.com', True))

        self.assertTrue(u.hash != u2.hash)
