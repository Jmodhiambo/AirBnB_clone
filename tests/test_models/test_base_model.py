#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def setUp(self):
        """Set up method for test cases"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if the instance is correctly created"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        """Test if id is unique"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_save(self):
        """Test if save updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        """Test if to_dict creates the correct dictionary"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_method(self):
        """Test the __str__ method"""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)


if __name__ == "__main__":
    unittest.main()
