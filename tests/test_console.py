#!/usr/bin/python3

"""
Module should contain the tests for console module
"""

import pycodestyle
import unittest


class TestConsole(unittest.TestCase):
    """
    Class contains the test suite for the console class
    """
    def test_console_compliance(self):
        """
        Function checks the compliance of the console file
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Style errors in console.")


if '__name__' == '__main__':
    unittest.main()
