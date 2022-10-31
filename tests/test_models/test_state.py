#!/usr/bin/python3

"""
Module should contain the tests for state module
"""


import unittest
import pycodestyle


class TestState(unittest.TestCase):
    """
    Test class for state model
    """
    def test_state_compliance(self):
        """
        Function tests pycodestyle compliance of State and tests
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(
            ["models/state.py", "tests/test_models/test_state.py"])
        self.assertEqual(
            result.total_errors, 0, "Style errors in state.py or state tests"
            )


if '__name__' == '__main__':
    unittest.main()
