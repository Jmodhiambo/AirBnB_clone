#!/usr/bin/python3
"""
This module updates the attributes of an instance.
"""

from models import storage
from models.classes import classes
import shlex


def update_instance(args):
    """
    Updates or adds an attribute to an instance based on the class name and ID.
    """
    args_list = shlex.split(args)
    if len(args_list) < 1:
        return "** class name missing **"
    if args_list[0] not in classes:
        return "** class doesn't exist **"
    if len(args_list) < 2:
        return "** instance id missing **"

    # Get the instance key
    class_name, instance_id = args_list[0], args_list[1]
    key = f"{class_name}.{instance_id}"
    obj_dict = storage.all()

    if key not in obj_dict:
        return "** no instance found **"
    if len(args_list) < 3:
        return "** attribute name missing **"
    if len(args_list) < 4:
        return "** value missing **"

    attribute_name, attribute_value = args_list[2], args_list[3].strip('"')

    # Prevent updating restricted attributes
    if attribute_name in ["id", "created_at", "updated_at"]:
        return ""

    # Get the instance and update the attribute
    instance = obj_dict[key]
    current_value = getattr(instance, attribute_name, None)

    # Cast the value to the type of the existing attribute
    if current_value is not None:
        if isinstance(current_value, int):
            attribute_value = int(attribute_value)
        elif isinstance(current_value, float):
            attribute_value = float(attribute_value)
        elif isinstance(current_value, str):
            attribute_value = str(attribute_value)

    # Set the attribute and save
    setattr(instance, attribute_name, attribute_value)
    instance.save()

    return ""
