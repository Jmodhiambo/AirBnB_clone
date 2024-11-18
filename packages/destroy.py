#!/usr/bin/python3
"""
This module provides functionality to delete an instance.
"""

from models import storage
from models.classes import classes
import shlex


def destroy_instance(args):
    """
    Deletes an instance based on class name and id.
    Args:
        args (str): The class name and id, separated by a space.
    Returns:
        str: Error message if any or None if successful.
    """
    args_list = shlex.split(args)
    if len(args_list) < 1:
        return "** class name missing **"
    class_name = args_list[0]

    if class_name not in classes:
        return "** class doesn't exist **"

    if len(args_list) < 2:
        return "** instance id missing **"
    instance_id = args_list[1]

    key = f"{class_name}.{instance_id}"
    obj_dict = storage.all()

    if key not in obj_dict:
        return "** no instance found **"

    # Delete the instance
    del obj_dict[key]
    storage.save()
    return ""
"""
def destroy_instance(args):
    ""
    Destroys an instance based on class name and id.
    The changes are saved into the JSON file.
    ""
    args_list = shlex.split(args)

    if len(args_list) == 0:
        return "** class name missing **"
    if args_list[0] not in classes:
        return "** class doesn't exist **"
    if len(args_list) == 1:
        return "** instance id missing **"

    # Constructiong the key for the instance
    class_name, instance_id = args_list[0], args_list[1]
    key = f"{class_name}.{instance_id}"

    # Check if the instance exists
    all_objects = storage.all()
    if key not in all_objects:
        return "** no instance found **"

    # Deletes the instance
    del all_objects[key]
    storage.save()
    return ""
"""
