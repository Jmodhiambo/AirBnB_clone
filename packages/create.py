#!/usr/bin/python3
"""
This is module of the create method is console.py
"""

from models import storage
from models.classes import classes


def create_instance(class_name):
    """
    Create a new instance of the given class.
    Saves the instance to storage and returns its ID.
    """
    if not class_name:  # No class name provided
        return "** class name missing **"
    if class_name not in classes:  # Class name doesn't exist
        return "** class doesn't exist **"

    # Dynamically create an instance of the class
    instance = classes[class_name]()
    instance.save()
    return instance.id
