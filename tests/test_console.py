#!/usr/bin/python3
"""Test for console"""
import unittest

from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
import os

stdout = StringIO()
console = HBNBCommand()


class ConsoleTestCase(unittest.TestCase):
    """Test console"""


    def setUp(self):
        """Set up for each test"""
        console.onecmd("create State name=\"California\"")


    def tearDown(self):
        """Tear down after each test"""
        console.onecmd("destroy State 123")


    def test_create(self):
        """Test create"""
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            with patch('sys.stdout', stdout):
                console.onecmd('create State name="California"')
            self.assertEqual(len(stdout.getvalue()), 43)


if __name__ == "__main__":
    unittest.main()