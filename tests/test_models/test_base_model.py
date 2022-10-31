#!/usr/bin/python3

"""
This module contains the test for BaseModel class
"""

import unittest
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """
    Test class for base_model and tests
    """
    def test_base_model_compliance(self):
        """
        Function tests pycodestyle compliance of BaseModel and tests
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(
            ["models/base_model.py", "tests/test_models/test_base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Style errors in BaseModel or tests"
            )


if '__name__' == '__main__':
    unittest.main()
