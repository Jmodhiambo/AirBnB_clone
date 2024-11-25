#!/usr/bin/python3
"""
This module has class FileStorage that:
    Serializes instances to a JSON file and;
    Deserializes JSON file to instances.
"""
import json
from models.classes import classes


class FileStorage():
    """
    Serializes instances to a JSON file and;
    Deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, only if the JSON file exists.
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                if class_name in classes:
                    self.__objects[key] = classes[class_name](**value)
        except FileNotFoundError:
            pass
