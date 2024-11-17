#!/usr/bin/python3
"""
This module prints the instances.
"""

from models import storage
from models.classes import classes


def all_instances(args):
    """
    Prints all instances and instances of class if the class is provided.
    """
    args_list = args.split()

    if len(args_list) == 0:
        obj_dict = storage.all()
        return [str(obj) for obj in obj_dict.values()]

    if len(args_list) == 1:
        class_name = args_list[0]
        if class_name not in classes:
            return "** class doesn't exist **"

        obj_dict = storage.all()
        filtered_objs = [
            str(obj) for key, obj in obj_dict.items()
            if key.startswith(f"{class_name}.")
        ]
        return filtered_objs
