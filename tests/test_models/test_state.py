#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up resources for testing"""
        self.state = State()

    def test_attributes(self):
        """Test default attributes"""
        self.assertEqual(self.state.name, "")

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.state, State)


if __name__ == "__main__":
    unittest.main()
