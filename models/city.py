#!/usr/bin/python3

"""
module contains the class definition for a city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    class holds the state_id and name attributes
    """
    state_id = ""
    name = ""
