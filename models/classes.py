#!/usr/bin/python3
"""
Maps class names to their respective classes.
"""

from models.base_model import BaseModel
from models.user import User


# Dictionary mapping class names to their classes
classes = {
    "BaseModel": BaseModel,
    "User": User
}
