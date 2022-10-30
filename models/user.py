#!/usr/bin/python3

"""
module contains the class definition for a user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class user holds data attributes for a users email
    password, first and last names
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
