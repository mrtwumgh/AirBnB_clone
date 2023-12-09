#!/usr/bin/python3
"""
A module that defines a class BaseModel
"""
from datetime import datetime
from . import storage
import uuid


class BaseModel:
    """
    A class that defines BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel
        """
        if kwargs:
            for key, v in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        self.updated_at = datetime.now()
        storage.save()

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
