#!/usr/bin/python3

"""
Module should contain the tests for amenity module
"""

import unittest
import pycodestyle


class TestAmenities(unittest.TestCase):
    """
    Test class for Amenities and tests
    """
    def test_amenities_compliance(self):
        """
        Function tests pycodestyle compliance of Amenity model and tests
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(
            ["models/amenity.py", "tests/test_models/test_amenity.py"])
        self.assertEqual(
            result.total_errors, 0, "Style errors in amenity.py or tests"
            )


if '__name__' == '__main__':
    unittest.main()
