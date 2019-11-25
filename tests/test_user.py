import unittest
from app.models import User

class test_user(unittest.TestCase):
    '''
    Test class to check whether the various functions of the user class run correctly
    '''
    def setUp(self):
        self.new_user = User(password = 'alex')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

        def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('alex'))