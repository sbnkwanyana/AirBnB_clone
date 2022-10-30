#!/usr/bin/python3
"""
Module contains the defenition of the BaseModel
used to define a base class for other classes
"""

from datetime import datetime
from uuid import uuid4


class BaseModel():
    """
    BaseModel serves as the parent class for
    all common attributes and functions of other classes
    """

    def __init__(self):
        """
        initializes a new instance of BaseModel with a unique id
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Prints object in the format [<class name>] (<self.id>) <self.__dict__>
        """
        print(
          "[{0}] ({1}) {2}"
          .format(self.__class__.__name__, self.id, self.__dict__)
          )

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dic(self):
        """
        returns a dictionary containing all keys/values with
        addition of __class__ = class name
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.strftime(
          '%Y-%m-%dT%H:%M:%S.%f')
        dic["updated_at"] = self.updated_at.strftime(
          '%Y-%m-%dT%H:%M:%S.%f')
        return dic
