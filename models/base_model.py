#!/usr/bin/python3
"""
A module that defines a class BaseModel
"""
import datetime
import uuid


class BaseModel:
    """
    A class that defines BaseModel
    """

    def __init__(self):
        """
        Constructor for BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        returns the string representation of object
        """
        s = "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        return s

    def save(self):
        """
        updates the public instance attribute updated_at
        with current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        self.__dict__["__class__"] = __class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
