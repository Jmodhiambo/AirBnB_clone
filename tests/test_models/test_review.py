#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up resources for testing"""
        self.review = Review()

    def test_attributes(self):
        """Test default attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.review, Review)


if __name__ == "__main__":
    unittest.main()
