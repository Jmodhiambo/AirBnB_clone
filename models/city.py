#!/usr/bin/python3
"""
Defines the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class representing a city.

    Attributes:
        state_id (str): The ID of the state this city belongs to.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
