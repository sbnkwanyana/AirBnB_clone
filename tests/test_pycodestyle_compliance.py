#!/usr/bin/python3
"""
This module contains the pycodestyle test class
"""

import unittest
import pycodestyle

class TestCodeFormat(unittest.TestCase):
     """
     class definition encapsulates the test functions for
     for pycodestyle checks on all python files
     """

     def test_console_compliance(self):
          """
          Function checks the compliance of the console file
          """
          style = pycodestyle.StyleGuide(quiet=True)
          result =  style.check_files(["console.py"])
          self.assertEqual(result.total_errors, 0, "There are code style errors in the console.")

     def test_models_compliance(self):
          """
          Function tests the compliance of all model files
          """
          style = pycodestyle.StyleGuide(quiet=True)
          result =  style.check_files(["models/"])
          self.assertEqual(result.total_errors, 0, "Found code style errors in models.")

     def test_test_compliance(self):
          """
          Function tests the compliance of all test files
          """
          style = pycodestyle.StyleGuide(quiet=True)
          result =  style.check_files(["test/"])
          self.assertEqual(result.total_errors, 0, "Found code style in tests.")
