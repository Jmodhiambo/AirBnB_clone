#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up resources for testing"""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test default attributes"""
        self.assertEqual(self.amenity.name, "")

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.amenity, Amenity)


if __name__ == "__main__":
    unittest.main()
