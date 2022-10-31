#!/usr/bin/python3

"""
Module should contain the tests for file storage module
"""


import unittest
import pycodestyle


class TestFileStorageEngine(unittest.TestCase):
    """
    Test class for FileStorageEngine
    """

    def test_file_storage_compliance(self):
        """
        Function tests pycodestyle compliance of FileStorage engine and tests
        """
        style = pycodestyle.StyleGuide()
        result = style.check_files(
            ["models/engine/file_storage.py",
             "tests/test_models/test_engine/test_file_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Style errors in FileStorage or tests"
            )


if '__name__' == '__main__':
    unittest.main()
