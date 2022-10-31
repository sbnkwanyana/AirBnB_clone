#!/usr/bin/python3

"""
Module should contain the tests for place module
"""


import unittest
import pycodestyle


class TestPlace(unittest.TestCase):
    """
    Test class for Place and tests
    """
    def test_place_compliance(self):
        """
        Function tests pycodestyle compliance of Place model and tests
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(
            ["models/place.py", "tests/test_models/test_place.py"])
        self.assertEqual(
            result.total_errors, 0, "Style errors in place.py or tests"
            )


if '__name__' == '__main__':
    unittest.main()
