#!/usr/bin/python3

"""
Module should contain the tests for review module
"""


import unittest
import pycodestyle


class TestReview(unittest.TestCase):
    """
    Test class for Review
    """
    def test_review_compliance(self):
        """
        Function tests pycodestyle compliance of review model and tests
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(
            ["models/review.py", "tests/test_models/test_review.py"])
        self.assertEqual(
            result.total_errors, 0, "Style errors in review.py or review tests"
            )


if '__name__' == '__main__':
    unittest.main()
