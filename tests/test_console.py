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
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsoleAdvanced(unittest.TestCase):
    """Unittests for the advanced functionality of console.py"""

    def setUp(self):
        """Set up test objects"""
        self.classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up resources"""
        storage.reload()

    def test_count(self):
        """Test the `count` command for all classes"""
        for cls_name, cls in self.classes.items():
            obj1 = cls()
            obj2 = cls()
            storage.new(obj1)
            storage.new(obj2)
            storage.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"{cls_name}.count()")
                output = f.getvalue().strip()
            self.assertEqual(int(output), 2)

    def test_show(self):
        """Test the `show` command for all classes"""
        for cls_name, cls in self.classes.items():
            obj = cls()
            storage.new(obj)
            storage.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"{cls_name}.show(\"{obj.id}\")")
                output = f.getvalue().strip()
            self.assertIn(obj.id, output)

    def test_show_invalid(self):
        """Test `show` command with invalid id"""
        for cls_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"{cls_name}.show(\"invalid_id\")")
                output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test the `destroy` command for all classes"""
        for cls_name, cls in self.classes.items():
            obj = cls()
            obj_id = obj.id
            storage.new(obj)
            storage.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"{cls_name}.destroy(\"{obj_id}\")")
            self.assertNotIn(f"{cls_name}.{obj_id}", storage.all())

    def test_update(self):
        """Test the `update` command for all classes"""
        for cls_name, cls in self.classes.items():
            obj = cls()
            obj_id = obj.id
            storage.new(obj)
            storage.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"{cls_name}.update(\"{obj_id}\", \"name\", \"TestName\")")
            self.assertEqual(storage.all()[f"{cls_name}.{obj_id}"].name, "TestName")

    def test_update_dict(self):
        """Test the `update` command with a dictionary"""
        for cls_name, cls in self.classes.items():
            obj = cls()
            obj_id = obj.id
            storage.new(obj)
            storage.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(
                    f"{cls_name}.update(\"{obj_id}\", {{\"name\": \"TestName\", \"number\": 42}})"
                )
            updated_obj = storage.all()[f"{cls_name}.{obj_id}"]
            self.assertEqual(updated_obj.name, "TestName")
            self.assertEqual(updated_obj.number, 42)

    def test_update_invalid_id(self):
        """Test `update` command with invalid id"""
        for cls_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"{cls_name}.update(\"invalid_id\", \"name\", \"TestName\")")
                output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == "__main__":
    unittest.main()
