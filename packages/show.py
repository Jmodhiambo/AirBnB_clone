#!/usr/bin/python3
"""
This module contains the show method for console.py.
"""

from models import storage
from models.classes import classes
import shlex


def show_instance(args):
    """
    Show the string representation of an instance.
    Args:
        args (str): Arguments containing the class name and ID.
    Returns:
        str: The string representation of the instance or an error message.
    """
    args_list = shlex.split(args)

    if len(args_list) == 0:
        return "** class name missing **"
    if args_list[0] not in classes:
        return "** class doesn't exist **"
    if len(args_list) == 1:
        return "** instance id missing **"

    key = f"{args_list[0]}.{args_list[1]}"
    obj_dict = storage.all()

    if key not in obj_dict:
        return "** no instance found **"

    return str(obj_dict[key])
