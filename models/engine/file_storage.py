#!/usr/bin/python3
"""
This module contains the file storage engine of the program
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
    Class serializes and deserializes objects to and from json
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all objects stored inside a dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Store in objects dictionary a new object
        """
        key = "{0}.{1}".format(obj.__class__.__name__, str(obj.id))
        self.__objects[key] = obj

    def save(self):
        """
        Obtains the dictionary of representation of each object
        serializes all object to json and saves to file
        """
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()

        with open(self.__file_path, "w+", encoding="utf-8") as file:
            json.dump(dic, file)

    def reload(self):
        """
        Opens a file for reading and deserializes the data to an object
        """
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    self.__objects[key] = eval(
                        value["__class__"])(**value)
        except FileNotFoundError:
            return
