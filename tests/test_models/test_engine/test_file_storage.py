#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up resources for testing"""
        self.storage = FileStorage()
        self.test_model = BaseModel()
        self.storage.new(self.test_model)

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test the all method"""
        all_objects = self.storage.all()
        self.assertIn(f"{self.test_model.__class__.__name__}.{self.test_model.id}", all_objects)

    def test_new(self):
        """Test the new method"""
        all_objects = self.storage.all()
        key = f"{self.test_model.__class__.__name__}.{self.test_model.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], self.test_model)

    def test_save(self):
        """Test the save method"""
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        # Create a BaseModel instance and save it
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()

        # Clear __objects and reload from file
        FileStorage._FileStorage__objects = {}
        self.file_storage.reload()

        # Verify the object was reloaded
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.file_storage.all())
        self.assertEqual(self.file_storage.all()[key].id, obj.id)


if __name__ == "__main__":
    unittest.main()
