#!/usr/bin/python3
"""
A module for the class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """
        returns the string representation of object
        """
        s = "[User] ({}) {}".format(self.id, self.__dict__)
        return s

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = __class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
