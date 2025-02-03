#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        new = self.value(first_name='John')
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        new = self.value(last_name='Doe')  # Corrected here
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        new = self.value(email='john@gmail.com')
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ test password """
        new = self.value(password='my_password')
        self.assertEqual(type(new.password), str)