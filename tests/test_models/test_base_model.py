#!/usr/bin/python3
"""Defines unnittests for models/base_model.py."""
import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """BaseModel testing setup.
        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        Creates a BaseModel instance for testing.
        """
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """BaseModel testing teardown.
        Restore original file.json.
        Delete the test BaseModel instance.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        del cls.storage
        del cls.base

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/base_model.py"])
        self.assertEqual(p.total_errors, 4, "fix pep8 style errors")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        self.assertEqual(str, type(self.base.id))
        self.assertEqual(datetime, type(self.base.created_at))
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.base, BaseModel)

    def test_two_models_are_unique(self):
        """Test that different BaseModel instances are unique."""
        b = BaseModel()
        self.assertNotEqual(self.base.id, b.id)
        self.assertLess(self.base.created_at, b.created_at)
        self.assertLess(self.base.updated_at, b.updated_at)

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        d = datetime.now()
        b = BaseModel("1", id="5", created_at=d.isoformat())
        self.assertEqual(b.id, "5")
        self.assertEqual(b.created_at, d)

    def test_str(self):
        """Test __str__ representation."""
        st = self.base.__str__()
        self.assertIn("[BaseModel] ({})".format(self.base.id), st)
        self.assertIn("'id': '{}'".format(self.base.id), st)
        self.assertIn("'created_at': {}".format(repr(self.base.created_at)), st)
        self.assertIn("'updated_at': {}".format(repr(self.base.updated_at)), st)

   # @unittest.skipIf(os.getenv("HBNB_ENV") is not None, "Testing DBStorage")
    def test_save(self):
        """Test save method."""
        ob = self.base.updated_at
        self.base.save()
        self.assertLess(ob, self.base.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(self.base.id), f.read())

    def test_to_dict(self):
        """Test to_dict method."""
        bd = self.base.to_dict()
        self.assertEqual(dict, type(bd))
        self.assertEqual(self.base.id, bd["id"])
        self.assertEqual("BaseModel", bd["__class__"])
        self.assertEqual(self.base.created_at.isoformat(),
                         bd["created_at"])
        self.assertEqual(self.base.updated_at.isoformat(),
                         bd["updated_at"])
        self.assertEqual(bd.get("_sa_instance_state", None), None)


if __name__ == "__main__":
    unittest.main()
