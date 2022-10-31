#!/usr/bin/python3

"""
This module contains the test for BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    BaseModel test cases
    """

    @classmethod
    def setUp(cls):
        """
        Used to set up test case attributes
        """
        cls.base_model = BaseModel()

    def test_id_str(self):
        """
        Asserts if the id is of type string
        """
        self.assertEqual(type(self.base_model.id), str)

    @classmethod
    def tearDown(cls):
        """
        used to discard test case attributes
        """
        del cls.base_model