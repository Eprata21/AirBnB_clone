#!/usr/bin/python3
"""Module for test User State class"""
import unittest
import json
import pep8
import datetime

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test State class implementation"""
    def test_docstrings(self):
        """check docstrings documentation"""
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def test_pep8_conformance_base_model(self):
        """Test that models/State.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/State.py'])
        self.assertEqual(result.total_errors, 1, "fix pep8")

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)

if __name__ == '__main__':
    unittest.main()
