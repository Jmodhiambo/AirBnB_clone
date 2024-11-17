#!/usr/bin/python3
"""
This module initializes the FileStorage system for the application.
"""

from models.engine.file_storage import FileStorage


# Create the singleton instance of FileStorage
storage = FileStorage()

# Load previously serialized objects
storage.reload()
