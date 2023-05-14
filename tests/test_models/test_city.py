#!/usr/bin/python3
"""Module for test User class"""
import unittest
import json
import pep8
import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test City class implementation"""

    def test_docstrings(self):
        """check docstrings documentation"""
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_pep8_conformance_base_model(self):
        """Test that models/user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
