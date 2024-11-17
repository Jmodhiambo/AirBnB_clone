#!/usr/bin/python3
"""
This module defines class BaseModel.
The class defines common attributes and methods for other classes.
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    This is class BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes attributes and methods for class BaseModel.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":  # Exclude the __class__ key
                    if key in ("created_at", "updated_at"):  # Handle datatime
                        val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Lazy import to avoid circular import issues
            from models import storage
            storage.new(self)  # Add new instance to storage

    def save(self):
        """
        Updates the attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()  # Save the storage data to file

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__.
        """
        obj_dict = self.__dict__.copy()  # Copy to avoid modifying the original
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        """
        The string magic.
        Prints [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
