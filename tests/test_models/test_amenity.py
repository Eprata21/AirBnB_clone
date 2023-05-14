#!/usr/bin/python3
"""Module for test Amenity class"""
import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test Amenity class implementation"""
    def test_docstrings(self):
        """check docstrings documentation"""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_pep8_conformance_base_model(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
             self.assertIsInstance(Amenity.name, str)

if __name__ == '__main__':
    unittest.main()
