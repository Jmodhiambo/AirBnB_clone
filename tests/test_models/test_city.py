#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up resources for testing"""
        self.city = City()

    def test_attributes(self):
        """Test default attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.city, City)


if __name__ == "__main__":
    unittest.main()
