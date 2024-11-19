#!/usr/bin/python3
"""
This module defines the function to update an instance.
"""

import shlex
from models import storage
from models.classes import classes


def update_instance(args):
    """
    Updates an instance based on class name and id by adding/updating attributes.
    Args:
        args (str): Class name, id, attribute name, and attribute value.
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
    instance_id = args_list[1].strip(",")  # Strip trailing commas

    key = f"{class_name}.{instance_id}"
    obj_dict = storage.all()

    if key not in obj_dict:
        return "** no instance found **"

    if len(args_list) < 3:
        return "** attribute name missing **"
    attribute_name = args_list[2].strip(",{}:")  # Strip trailing commas

    if attribute_name in {"id", "created_at", "updated_at"}:
        # Restrict updates to these attributes
        return None

    if len(args_list) < 4:
        return "** value missing **"
    attribute_value = args_list[3].strip(",")  # Strip trailing commas

    # Update the instance with the new attribute and value
    obj = obj_dict[key]
    try:
           # Check if the attribute exists in the instance or its class
           if hasattr(obj, attribute_name):
               attr_type = type(getattr(obj, attribute_name, None))
               # Cast the value to the correct type if it's a primitive type
               if attr_type in [int, float, bool, str]:
                   attribute_value = attr_type(attribute_value)
    except (ValueError, SyntaxError, NameError):
        pass

    setattr(obj, attribute_name, attribute_value)
    obj.save()
    return ""
