#!/usr/bin/python3
"""
"""

import json

class FileStorage():
    """
    """
    __file_path = "file.json"
    __objects = { }

    def all(self):
        """
        Returns all objects stored inside a dictionary
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Store in objects dictionary a new object
        """
        key = "{0}.{1}".format(obj.__class__.__name__, str(obj.id))
        FileStorage.__objects[key] = obj
    
    def save(self):
        """
        Obtains the dictionary of representation of each object
        serializes all object to json and saves to file
        """
        dic = { }
        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()

        with open(
            FileStorage.__file_path, "w", encoding="UTF-8"
            ) as file_write:
            json.dump(dic, file_write)


    def reload(self):
        """
        Opens a file for reading and deserializes the data to an object
        """
        try:
            with open(
                FileStorage.__file_path, "r", encoding="UTF-8"
                ) as file_read:
                data = json.load(file_read)
                for key, value in data.items():
                    FileStorage.__objects[key] = eval(
                        value["__class__"])(**value)
        except FileNotFoundError:
            return