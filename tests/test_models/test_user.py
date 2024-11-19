#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up resources for testing"""
        self.user = User()

    def test_attributes(self):
        """Test default attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.user, User)


if __name__ == "__main__":
    unittest.main()
