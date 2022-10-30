#!/usr/bin/python3

"""
module contains the class definition for a review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class holds an reviews place_id
    user_id and text
    """
    place_id = ""
    user_id = ""
    text = ""
