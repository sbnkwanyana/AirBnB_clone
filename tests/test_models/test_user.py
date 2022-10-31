#!/usr/bin/python3

"""
Module should contain the tests for user module
"""


import unittest
import pycodestyle


class TestUser(unittest.TestCase):
    """
    Test class for User
    """
    def test_user_compliance(self):
        """
        Function tests pycodestyle compliance of User model and tests
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(
            ["models/user.py", "tests/test_models/test_user.py"])
        self.assertEqual(
            result.total_errors, 0, "Style errors in user.py or user tests"
            )


if '__name__' == '__main__':
    unittest.main()
