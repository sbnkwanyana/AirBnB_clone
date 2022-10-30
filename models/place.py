#!/usr/bin/python3

"""
module contains the class definition for an place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    class holds a places city_id, user_id, name, description
    number_rooms, nuber_bathrooms, max_guest, price_by_night
    latitude, longitude and list of amenities_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenities_ids = []
