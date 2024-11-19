#!/usr/bin/python3
"""
Unittests for console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Unittests for the HBNBCommand console"""

    def setUp(self):
        """Set up resources for testing"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up resources after testing"""
        try:
            storage.save()
        except Exception:
            pass

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue()
        self.assertIn("Documented commands", output)

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
        self.assertTrue(len(output) > 0)  # Should return an id
        obj = storage.all().get(f"BaseModel.{output}")
        self.assertIsNotNone(obj)

    def test_show(self):
        """Test show command"""
        obj = BaseModel()
        obj_key = f"BaseModel.{obj.id}"
        storage.new(obj)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj.id}")
            output = f.getvalue().strip()
        self.assertIn(obj_key, output)

    def test_show_missing_class(self):
        """Test show command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_missing_id(self):
        """Test show command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel invalid_id")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test destroy command"""
        obj = BaseModel()
        storage.new(obj)
        obj_key = f"BaseModel.{obj.id}"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {obj.id}")
        self.assertNotIn(obj_key, storage.all())

    def test_all(self):
        """Test all command"""
        obj1 = BaseModel()
        obj2 = User()
        storage.new(obj1)
        storage.new(obj2)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue()
        self.assertIn(f"BaseModel.{obj1.id}", output)
        self.assertIn(f"User.{obj2.id}", output)

    def test_all_with_class(self):
        """Test all command with specific class"""
        obj1 = BaseModel()
        obj2 = User()
        storage.new(obj1)
        storage.new(obj2)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            output = f.getvalue()
        self.assertIn(f"BaseModel.{obj1.id}", output)
        self.assertNotIn(f"User.{obj2.id}", output)

    def test_update(self):
        """Test update command"""
        obj = BaseModel()
        storage.new(obj)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj.id} name 'MyModel'")
        self.assertEqual(storage.all()[f"BaseModel.{obj.id}"].name, "MyModel")

    def test_update_missing_class(self):
        """Test update command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_update_missing_id(self):
        """Test update command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update command with invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel invalid_id name 'MyModel'")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")


if __name__ == "__main__":
    unittest.main()
