#!/usr/bin/python3

"""
Module should contain the tests for city module
"""


import unittest
import pycodestyle


class TestCity(unittest.TestCase):
    """
    Test class for Ciy and tests
    """
    def test_city_compliance(self):
        """
        Function tests pycodestyle compliance of City Model and tests
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(
            ["models/city.py", "tests/test_models/test_city.py"])
        self.assertEqual(
            result.total_errors, 0, "Style errors in city.py or tests"
            )


if '__name__' == '__main__':
    unittest.main()
